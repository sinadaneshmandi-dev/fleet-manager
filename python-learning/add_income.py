import db
import utility
import sqlite3

def run():
    rows = db.list_vehicles()
    utility.print_vehicle(rows)
    vehicle_id, date, amount, note = utility.insert_income()
    try:
        db.add_income(vehicle_id, date, amount, note)
        print("اطلاعات با موفقیت اضافه شد")
    except sqlite3.IntegrityError:
        print("اطلاعات ذخیره نشد دوباره امتحان کنید")


if __name__ == "__main__":
    run()
