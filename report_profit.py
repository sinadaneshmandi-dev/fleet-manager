from pathlib import Path
import db

BASE = Path(__file__).resolve().parent
REPORT_SQL = BASE / "sql" / "report.sql"


def get_report_profit():
    query = REPORT_SQL.read_text(encoding="utf-8")
    conn = db.connect()
    try:
        return conn.execute(query).fetchall()
    finally:
        conn.close()
