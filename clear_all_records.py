import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE / "fleet.db"

def Clear_db():
    conn = sqlite3.connect(DB_PATH)
    schema = (BASE/"sql"/"clear_records.sql").read_text(encoding="utf-8")
    conn.executescript(schema)
    conn.commit()
    conn.close()

def run():
    Clear_db()

if __name__ == "__main__":
    run()