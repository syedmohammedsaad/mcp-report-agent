from datetime import date
import report

ROWS = [
    {"task": "A", "owner": "X", "status": "done", "due": "2026-01-01"},
    {"task": "B", "owner": "X", "status": "todo", "due": "2026-01-01"},
    {"task": "C", "owner": "Y", "status": "todo", "due": "bad-date"},
    {"task": "D", "owner": "Y", "status": "todo", "due": "2030-01-01"},
]

def test_overdue_ignores_done_and_bad_dates():
    od = report.find_overdue(ROWS, date(2026, 6, 1))
    assert [r["task"] for r in od] == ["B"]

def test_report_counts_and_sections():
    text = report.build_report(ROWS, date(2026, 6, 1))
    assert "Total tasks: 4" in text and "todo: 3" in text and "- B (X, due 2026-01-01)" in text

def test_missing_column(tmp_path):
    p = tmp_path / "bad.csv"; p.write_text("task,owner\nA,B\n")
    try:
        report.load_tasks(p); assert False
    except ValueError as e:
        assert "status" in str(e)
