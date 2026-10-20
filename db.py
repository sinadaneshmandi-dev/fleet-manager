import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE/"fleet.db"

def list_vehicles():
    conn = sqlite3.connect(DB_PATH)
    query = ("SELECT name, id FROM vehicles;")
    rows = conn.execute(query).fetchall()
    conn.close()
    return rows   

def print_vehical(rows):
    print(f"{'Vehicle':<12}")
    for name, id in rows:
        print(f"{name:<12}{id:<12}")