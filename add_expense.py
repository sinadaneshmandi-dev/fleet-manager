import db
import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE/"fleet.db"


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
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute("INSERT INTO expenses(vehicle_id, date, category, amount,note) VALUES(? , ? , ? , ? , ?)", expense)
        conn.commit()
        print("information saved successfully")
    except  sqlite3.IntegrityError:
        print("information didn't save cause to an input error, plz insert true inputs.")
    finally:
       conn.close()
            
    

if __name__ == "__main__":
    rows = db.list_vehicles()
    db.print_vehical(rows)
    expense = ask_expense()
    save_expense(expense)
    print(expense)
