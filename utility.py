def ask_expense():
    while True:
        try:
            expense_id = int(input("لطفا شناسه هزینه ای که میخوای پاک بکنی رو وارد کن : "))
            break        
        except:
            print("لطفا شماره شناسه رو دوباره وارد کن")
    return expense_id

def ask_income():
    while True:
        
        try:
            income_id = int(input("لطفا عدد شناسه دریافت را برای حذف کردن وارد کنید : "))
            break
        except:
            print("شناسه دریافت باید عدد باشد دوباره امتحان کنید.")
    return income_id

def ask_vehicle():
    while True:
        try:
            vehicle_id = int(input("لطفا شماره ماشینی که میخواهید حذف کنید را وارد کنید:"))
            break
        except:
            print(" خطا!!! لطفا دوباره امتحان کنید")
    return vehicle_id

def insert_expense():
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

def insert_income():
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

def insert_vehicle():
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

def print_expense(rows):
    print(f"{'شناسه':<12}")
    for id , vehicle_id, date, category, amount in rows:
        print(f"{id:<12}{vehicle_id:<12}{date:<12}{category:<12}{amount:<12}")

def print_income(rows):
    print(f"{'شناسه':<12}")
    for id , vehicle_id, date, amount in rows:
        print(f"{id:<12}{vehicle_id:<12}{date:<12}{amount:<12}")

def print_vehicle(rows):
    print(f"{'شناسه':<12}")
    for name, id in rows:
        print(f"{name:<12}{id:<12}") 

def ask_id(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("لطفاً یک عدد وارد کنید.")


def ask_text_or_keep(prompt, old_value):
    text = input(f"{prompt} [{old_value or ''}]: ").strip()
    return text or old_value


def ask_int_or_keep(prompt, old_value):
    while True:
        text = input(f"{prompt} [{old_value}]: ").strip()
        if text == "":
            return old_value
        try:
            return int(text)
        except ValueError:
            print("لطفاً یک عدد وارد کنید.")