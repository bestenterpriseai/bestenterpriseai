#!/usr/bin/env python3
"""Validate a minimal Enterprise AI tool contract."""
import argparse
import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = ["name", "version", "owner", "risk_tier", "description", "input_schema", "approval", "audit"]
ALLOWED_RISK_TIERS = {"low", "medium", "high", "critical"}


def validate(contract):
    errors = []
    for field in REQUIRED_TOP_LEVEL:
        if field not in contract:
            errors.append(f"missing required field: {field}")
    risk = contract.get("risk_tier")
    if risk not in ALLOWED_RISK_TIERS:
        errors.append(f"risk_tier must be one of {sorted(ALLOWED_RISK_TIERS)}")
    schema = contract.get("input_schema", {})
    if schema.get("type") != "object":
        errors.append("input_schema.type must be object")
    if contract.get("risk_tier") in {"high", "critical"} and not contract.get("approval", {}).get("required_when"):
        errors.append("high/critical tools must define approval.required_when")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate an Enterprise AI tool contract")
    parser.add_argument("contract", help="Path to tool contract JSON")
    args = parser.parse_args(argv)

    data = json.loads(Path(args.contract).read_text(encoding="utf-8"))
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"OK: {data['name']} {data['version']} ({data['risk_tier']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
