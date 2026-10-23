import sqlite3
import utility
import db

def run():
    rows = db.list_vehicles()
    utility.print_vehicle(rows)
    name,plate,typeV,odometer_km = utility.insert_vehicle()
    try:
        db.add_vehicle(name,plate,typeV,odometer_km)
        print("اطلاعات با موفقیت ذخیره شد")
    except sqlite3.IntegrityError:
        print("اطلاعات ذخیره نشد دوباره تلاش کنید")

if __name__ == "__main__":
    run()
    