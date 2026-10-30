import db
import sqlite3
import utility

def run():
    rows = db.list_vehicles()
    utility.print_vehicle(rows)
    vehicle_id = utility.ask_vehicle()
    try:
        deleted = db.delete_vehicle(vehicle_id)
        if deleted == 0:
            print("ماشینی با این شناسه وجود نداشت")
        else:
            print("هزینه با موفقیت پاک شد")
    except sqlite3.IntegrityError:
        print("این ماشین هزینه یا درآمد ثبت‌شده دارد؛ اول آن‌ها را حذف کنید")

if __name__ == "__main__":
    run()
    