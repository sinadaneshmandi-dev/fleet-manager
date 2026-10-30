import sqlite3
import db
import utility


def run():
    utility.print_expense(db.list_expenses())
    expense_id = utility.ask_id("شناسه‌ی هزینه‌ای که می‌خواهید ویرایش کنید: ")

    row = db.select_expense(expense_id)
    if row is None:
        print("هزینه‌ای با این شناسه وجود ندارد.")
        return

    _, old_vehicle_id, old_date, old_category, old_amount, old_note = row

    print("برای نگه داشتن مقدار فعلی فقط Enter بزنید.")
    vehicle_id = utility.ask_int_or_keep("شماره ماشین", old_vehicle_id)
    date = utility.ask_text_or_keep("تاریخ (YYYY-MM-DD)", old_date)
    category = utility.ask_text_or_keep("دسته", old_category)
    amount = utility.ask_int_or_keep("مبلغ", old_amount)
    note = utility.ask_text_or_keep("توضیح", old_note)

    try:
        updated = db.update_expense(expense_id, vehicle_id, date, category, amount, note)
    except sqlite3.IntegrityError:
        print("شماره ماشین معتبر نیست؛ چیزی تغییر نکرد.")
        return

    if updated == 0:
        print("هزینه‌ای با این شناسه وجود نداشت.")
    else:
        print("هزینه با موفقیت ویرایش شد.")


if __name__ == "__main__":
    run()