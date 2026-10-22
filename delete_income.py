import sqlite3
import db


def ask_income():
    while True:
        
        try:
            income_id = int(input("لطفا عدد شناسه دریافت را برای حذف کردن وارد کنید : "))
            break
        except:
            print("شناسه دریافت باید عدد باشد دوباره امتحان کنید.")
    return income_id

def run():
    db.show_income()
    income_id = ask_income()
    try:
        deleted = db.delete_income(income_id)
        if deleted == 0:
            print("دریافتی با این شناسه وجود نداشت")
        else:
            print("هزینه با موفقیت پاک شد")
    except sqlite3.IntegrityError:
        print("اطلاعات دریافت پاک نشد دوباره امتحان کنید")

if __name__ == "__main__":
    run()