import db
import sqlite3

def ask_income():
    while True:
        try:
            vehicle_id = int(input("Vehicle number: "))
            break
        except ValueError:
            print("plz enter a number: ")

    date = input("Date (YYYY-MM-DD): ")

    while True:
        try:
            amount = int(input("plz enter the amount of your income: "))
            break
        except ValueError:
            print("plz enter a number :")

    note = input("what is it for :")
    return vehicle_id, date,amount, note 

def run():
    db.list_vehicles()
    vehicle_id, date, amount, note = ask_income()
    try:
        db.add_income(vehicle_id, date, amount, note)
        print("اطلاعات با موفقیت اضافه شد")
    except sqlite3.IntegrityError:
        print("اطلاعات ذخیره نشد دوباره امتحان کنید")


if __name__ == "__main__":
    run()
