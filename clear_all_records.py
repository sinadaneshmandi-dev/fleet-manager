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
    confirm = input("ایا مطمعنی که میخوای کل داده هات رو پاک کنی ؟ ؛ اگر مطمعنی بنویس (بله)").strip()
    if confirm == "بله":
        Clear_db()
    else:
        print("خب خداروشکر مواظب باش دوباره اشتباه کلیدی رو نزنی")
        return None
    

if __name__ == "__main__":
    run()