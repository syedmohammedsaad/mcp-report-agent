# AGENTS.md
- Keep business logic in `report.py`; `server.py` only wraps it as MCP tools.
- Never crash on a bad row: skip it and keep going (a past agent mistake).
- Every new tool needs a test in `test_report.py`. Run `pytest` before committing.
- Dates are ISO format (YYYY-MM-DD). Do not add new dependencies without asking.
