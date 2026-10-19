import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE / "fleet.db"

def get_report():
    conn = sqlite3.connect(DB_PATH)
    query = (BASE/"report.sql").read_text(encoding="utf-8")
    rows = conn.execute(query).fetchall()
    conn.close()
    return rows

def print_report(rows):
    print(f"{'Vehicle':<12}{'Income':>14}{'Expense':>14}{'Profit':>14}")
    for name, income, expense, profit in rows:
        print(f"{name:<12}{income:>14,}{expense:>14,}{profit:>14,}")
if __name__ == "__main__":
    rows = get_report()
    print_report(rows)
