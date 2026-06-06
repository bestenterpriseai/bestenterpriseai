#!/usr/bin/env python3
"""Compute small SLO report from Enterprise AI trace JSONL."""
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
    parser = argparse.ArgumentParser(description="Summarize agent SLOs from trace events")
    parser.add_argument("traces", help="JSONL trace file")
    args = parser.parse_args(argv)

    events = list(load_jsonl(args.traces))
    if not events:
        print("no events", file=sys.stderr)
        return 1

    total = len(events)
    failures = sum(1 for event in events if event.get("status") not in {"success", "ok", "allowed"})
    tool_calls = [event for event in events if event.get("event_type") == "tool_call"]
    policy_blocks = sum(1 for event in events if event.get("policy_decision") == "block")
    total_cost = sum(float(event.get("cost_usd", 0) or 0) for event in events)
    latencies = [float(event.get("latency_ms", 0) or 0) for event in events]
    avg_latency = sum(latencies) / len(latencies)

    report = {
        "events": total,
        "failure_rate": failures / total,
        "tool_calls": len(tool_calls),
        "policy_blocks": policy_blocks,
        "total_cost_usd": round(total_cost, 6),
        "average_latency_ms": round(avg_latency, 2),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
