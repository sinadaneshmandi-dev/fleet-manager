import db
import utility

def run():
    expense_id = utility.ask_expense()
    expense = db.select_expense(expense_id)
    if not expense :
        print("شناسه هزینه پیدا نشد")
    else:
        utility.print_expense(expense)

if __name__ == "__main__":
    run()
