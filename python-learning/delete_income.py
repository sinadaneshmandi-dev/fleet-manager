import sqlite3
import db
import utility

def run():
    rows = db.list_incomes()
    utility.print_income(rows)
    income_id = utility.ask_income()
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