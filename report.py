"""Core logic: turn a task CSV into a weekly status report. No MCP dependency, so it is easy to test."""
import csv
from collections import Counter
from datetime import date


def load_tasks(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for col in ("task", "owner", "status", "due"):
        if rows and col not in rows[0]:
            raise ValueError(f"Missing required column: {col}")
    return rows


def find_overdue(rows, today=None):
    today = today or date.today()
    out = []
    for r in rows:
        if r["status"].strip().lower() == "done":
            continue
        try:
            if date.fromisoformat(r["due"].strip()) < today:
                out.append(r)
        except ValueError:
            continue  # skip rows with a bad date instead of crashing
    return out


def build_report(rows, today=None):
    status = Counter(r["status"].strip().lower() for r in rows)
    owners = Counter(r["owner"].strip() for r in rows if r["status"].strip().lower() != "done")
    overdue = find_overdue(rows, today)
    lines = ["# Weekly Status Report", "", f"Total tasks: {len(rows)}", ""]
    lines += [f"- {k}: {v}" for k, v in sorted(status.items())]
    lines += ["", "## Open work by owner"] + [f"- {o}: {n}" for o, n in owners.most_common()]
    lines += ["", "## Overdue"] + ([f"- {r['task']} ({r['owner']}, due {r['due']})" for r in overdue] or ["- None"])
    return "\n".join(lines)
