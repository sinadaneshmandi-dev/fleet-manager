import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE / "fleet.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    schema = (BASE/"schema.sql").read_text(encoding="utf-8")
    conn.executescript(schema)
    conn.commit()
    conn.close()
if __name__ == "__main__":
    init_db()
    print("Database created:",DB_PATH)