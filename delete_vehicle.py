import db
import sqlite3

def ask_vehicle():
    while True:
        try:
            vehicle_id = int(input("لطفا شماره ماشینی که میخواهید حذف کنید را وارد کنید:"))
            break
        except:
            print(" خطا!!! لطفا دوباره امتحان کنید")
    return vehicle_id

def run():
    db.list_vehicles()
    vehicle_id = ask_vehicle()
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
    