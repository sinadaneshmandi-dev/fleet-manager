import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE/"fleet.db"

def ask_vehicle():
    name = input("plz enter your vehicle name : ")
    plate = input("what is your vehicle plate( 00Q000 ) : ")
    type = input("plz enter the vehicle type << کامیون / اتوبوس >> : ")


    while True:
        try:
            odometer_km = int(input("plz enter the amount of your vehicle km_counter : "))
            break
        except ValueError:
            print("plz enter a number :")

    return name,plate,type,odometer_km

def save_vehicles(vehicle):
    conn = sqlite3.connect(DB_PATH)
    try:
            conn.execute("PRAGMA foreign_keys = ON")
            conn.execute("INSERT INTO vehicles(id,name,plate,type,odometer_km) VALUES(?,?,?,?)", vehicle)
            conn.commit()
            print("information saved successfully")
    except sqlite3.IntegrityError:
        print("information didn't save cause to an input error, plz insert true inputs.")
    finally:
           conn.close()
    

if __name__ == "__main__":
    vehicle = ask_vehicle()
    save_vehicles(vehicle)
    print(vehicle)