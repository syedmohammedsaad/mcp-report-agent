"""MCP server that exposes the report tools to any MCP-compatible AI agent (Claude Code, Cursor, etc.)."""
from mcp.server.fastmcp import FastMCP
import report

mcp = FastMCP("report-agent")


@mcp.tool()
def weekly_report(csv_path: str) -> str:
    """Build a markdown status report from a CSV with columns: task, owner, status, due (YYYY-MM-DD)."""
    return report.build_report(report.load_tasks(csv_path))


@mcp.tool()
def overdue_tasks(csv_path: str) -> list[dict]:
    """List tasks that are not done and past their due date."""
    return report.find_overdue(report.load_tasks(csv_path))


if __name__ == "__main__":
    mcp.run()
