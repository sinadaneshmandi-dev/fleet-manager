import db
import utility

def run():
    vehicle_id = utility.ask_vehicle()
    vehicle = db.select_vehicle(vehicle_id)
    if not vehicle:
        print("شناسه ماشین پیدا نشد")
    else:
        utility.print_vehicle(vehicle)

if __name__ == "__main__":
    run()