# Executable Examples

This folder contains lightweight starter scripts for Enterprise AI governance, evals, red teaming, observability, and inference smoke testing.

These scripts are intentionally dependency-light and safe by default. They do not call external model APIs unless you adapt them.

## Scripts

| Script | Purpose |
| --- | --- |
| `eval_harness.py` | Scores JSONL eval cases for expected and forbidden content. |
| `tool_contract_validator.py` | Validates required fields in a tool contract JSON file. |
| `red_team_harness.py` | Runs simple red-team case checks and prints pass/fail controls. |
| `trace_replay.py` | Filters and prints trace events by trace ID. |
| `agent_slo_report.py` | Computes basic SLO metrics from trace JSONL. |
| `vllm_smoke_test.ps1` | Tests an OpenAI-compatible vLLM endpoint from PowerShell. |

## Commands

```powershell
python -m py_compile examples\*.py
python examples\eval_harness.py evals\sample_eval_cases.jsonl
python examples\tool_contract_validator.py examples\sample_tool_contract.json
python examples\red_team_harness.py evals\sample_red_team_cases.jsonl
python examples\trace_replay.py examples\sample_traces.jsonl --trace-id trace-001
python examples\agent_slo_report.py examples\sample_traces.jsonl
```

## Safety

- Treat these as reference implementations, not production controls.
- Add authentication, authorization, logging, and error handling before production use.
- Do not put secrets in sample files.
