import db
import utility

def run():
    income_id = utility.ask_income()
    income = db.select_income(income_id)
    if not income:
        print("شناسه دریافت پیدا نشد")
    else:
        utility.print_income(income)

if __name__ == "__main__":
    run()