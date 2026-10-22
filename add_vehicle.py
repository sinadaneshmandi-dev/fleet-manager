import sqlite3
import db


def ask_vehicle():
    name = input("plz enter your vehicle name : ")
    plate = input("what is your vehicle plate( 00Q000 ) : ")
    typeV = input("plz enter the vehicle type << کامیون / اتوبوس >> : ")


    while True:
        try:
            odometer_km = int(input("plz enter the amount of your vehicle km_counter : "))
            break
        except ValueError:
            print("plz enter a number :")

    return name,plate,typeV,odometer_km

def run():
    rows = db.list_vehicles()
    db.print_vehical(rows)
    name,plate,typeV,odometer_km = ask_vehicle()
    try:
        db.add_vehicle(name,plate,typeV,odometer_km)
        print("اطلاعات با موفقیت ذخیره شد")
    except sqlite3.IntegrityError:
        print("اطلاعات ذخیره نشد دوباره تلاش کنید")

if __name__ == "__main__":
    run()
    