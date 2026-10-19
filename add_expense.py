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

def ask_expense():
    while True:
        try:
            vehicle_id = int(input("Vehicle number: "))
            break
        except ValueError:
            print("plz enter a number: ")

    date = input("Date (YYYY-MM-DD): ")

    category = input("plz add category: (سوخت) or (تعمیر) or ...")

    while True:
        try:
            amount = int(input("plz enter the amount of your expens: "))
            break
        except ValueError:
            print("plz enter a number :")

    note = input("what is it for :")
    return vehicle_id, date, category, amount, note 

def save_expense(expense):
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    # TODO 1: یه INSERT بنویس
    conn.execute("INSERT INTO expenses(vehicle_id, date, category, amount,note) VALUES(? , ? , ? , ? , ?)", expense)
    conn.commit()
    # TODO 2: تغییرات رو ذخیره کن
    conn.close()

if __name__ == "__main__":
    rows = list_vehicles()
    print_vehical(rows)
    expense = ask_expense()
    save_expense(expense)
    print(expense)
