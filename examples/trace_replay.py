#!/usr/bin/env python3
"""Replay or filter JSONL trace events."""
import argparse
import json
import sys
from pathlib import Path


def load_jsonl(path):
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Replay Enterprise AI trace events")
    parser.add_argument("traces", help="JSONL trace file")
    parser.add_argument("--trace-id", help="Only show one trace_id")
    args = parser.parse_args(argv)

    count = 0
    for event in load_jsonl(args.traces):
        if args.trace_id and event.get("trace_id") != args.trace_id:
            continue
        count += 1
        print(json.dumps(event, indent=2, sort_keys=True))
    if count == 0:
        print("no matching trace events", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
