import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE / "fleet.db"

def seed_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript((BASE /"sql"/ "seed.sql").read_text(encoding="utf-8"))
    conn.commit()
    conn.close()

def run():
    seed_db()
    print("Seed data inserted.")

if __name__ == "__main__":
    run()