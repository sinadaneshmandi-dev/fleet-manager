import sqlite3 
import db


def ask_expense():
    while True:
        try:
            expense_id = int(input("لطفا شناسه هزینه ای که میخوای پاک بکنی رو وارد کن : "))
            break        
        except:
            print("لطفا شماره شناسه رو دوباره وارد کن")
    return expense_id


def run():
    db.show_expenses()
    expense_id = ask_expense()
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