import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE / "fleet.db"

def get_report_profit():
    conn = sqlite3.connect(DB_PATH)
    query = (BASE/"sql"/"report.sql").read_text(encoding="utf-8")
    rows = conn.execute(query).fetchall()
    conn.close()
    return rows

def print_report_profit(rows):
    print(f"{'Vehicle':<12}{'Income':>14}{'Expense':>14}{'Profit':>14}")
    for name, income, expense, profit in rows:
        print(f"{name:<12}{income:>14,}{expense:>14,}{profit:>14,}")

def run():
    rows = get_report_profit()
    print_report_profit(rows)
if __name__ == "__main__":
    run()
