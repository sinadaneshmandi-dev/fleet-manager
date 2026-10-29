import db
import utility


def run():
    utility.print_vehicle(db.list_vehicles())
    vehicle_id = utility.ask_id("شماره‌ی ماشینی که می‌خواهید ویرایش کنید: ")

    row = db.get_vehicle(vehicle_id)
    if row is None:
        print("ماشینی با این شماره وجود ندارد.")
        return

    _, old_name, old_plate, old_type, old_odometer = row

    print("برای نگه داشتن مقدار فعلی فقط Enter بزنید.")
    name = utility.ask_text_or_keep("نام ماشین", old_name)
    plate = utility.ask_text_or_keep("پلاک", old_plate)
    typeV = utility.ask_text_or_keep("نوع (کامیون / اتوبوس)", old_type)
    odometer_km = utility.ask_int_or_keep("کیلومتر", old_odometer)

    if odometer_km < 0:
        print("کیلومتر نمی‌تواند منفی باشد؛ چیزی تغییر نکرد.")
        return

    updated = db.update_vehicle(vehicle_id, name, plate, typeV, odometer_km)
    if updated == 0:
        print("ماشینی با این شماره وجود نداشت.")
    else:
        print("ماشین با موفقیت ویرایش شد.")


if __name__ == "__main__":
    run()