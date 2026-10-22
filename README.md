# MCP Report Agent
A small Python MCP server that lets an AI agent turn a task CSV into a weekly status report and list overdue work.

## Run
    pip install -r requirements.txt
    pytest
    python server.py

## Connect to Claude Code
    claude mcp add report-agent -- python /full/path/to/server.py

Then ask: "Use weekly_report on sample_tasks.csv".

## Tools
- `weekly_report(csv_path)`: markdown summary by status, owner and overdue items
- `overdue_tasks(csv_path)`: tasks not done and past due
