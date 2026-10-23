import sqlite3 
import db
import utility

def run():
    rows = db.list_expenses()
    utility.print_expense(rows)
    expense_id = utility.ask_expense()
    try:
        deleted = db.delete_expense(expense_id)
        if deleted == 0:
            print("هزینه ای با این شناسه وجود نداشت")
        else:
            print("هزینه با موفقیت پاک شد")
    except  sqlite3.IntegrityError:
        print("هزینه ای به مشخصه ورودی شما در حافظه وجود نداشت")

if __name__ == "__main__":
    run()