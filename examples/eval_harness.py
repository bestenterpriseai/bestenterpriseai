#!/usr/bin/env python3
"""Tiny JSONL eval harness for Enterprise AI examples."""
import argparse
import json
import sys
from pathlib import Path


def load_jsonl(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.strip()
            if not line:
                continue
            try:
                yield line_no, json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path}:{line_no}: invalid JSON: {exc}") from exc


def score_case(case):
    output = str(case.get("output", "")).lower()
    expected = [str(item).lower() for item in case.get("expected_keywords", [])]
    forbidden = [str(item).lower() for item in case.get("forbidden_keywords", [])]
    citation_required = bool(case.get("citation_required", False))

    missing = [item for item in expected if item not in output]
    present_forbidden = [item for item in forbidden if item in output]
    has_citation = ("http://" in output or "https://" in output or "[" in output) if citation_required else True
    passed = not missing and not present_forbidden and has_citation
    return {
        "id": case.get("id", "unknown"),
        "passed": passed,
        "missing_keywords": missing,
        "forbidden_keywords": present_forbidden,
        "citation_ok": has_citation,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run simple Enterprise AI eval cases")
    parser.add_argument("cases", help="JSONL file with eval cases")
    args = parser.parse_args(argv)

    results = [score_case(case) for _, case in load_jsonl(args.cases)]
    passed = sum(1 for result in results if result["passed"])
    for result in results:
        status = "PASS" if result["passed"] else "FAIL"
        print(f"{status} {result['id']}: {json.dumps(result, sort_keys=True)}")
    print(f"summary: {passed}/{len(results)} passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
