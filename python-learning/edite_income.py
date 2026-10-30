import sqlite3
import db
import utility


def run():
    utility.print_income(db.list_incomes())
    income_id = utility.ask_id("شناسه‌ی درآمدی که می‌خواهید ویرایش کنید: ")

    row = db.select_income(income_id)
    if row is None:
        print("درآمدی با این شناسه وجود ندارد.")
        return

    _, old_vehicle_id, old_date, old_amount, old_note = row

    print("برای نگه داشتن مقدار فعلی فقط Enter بزنید.")
    vehicle_id = utility.ask_int_or_keep("شماره ماشین", old_vehicle_id)
    date = utility.ask_date_or_keep("تاریخ (YYYY-MM-DD)", old_date)
    amount = utility.ask_int_or_keep("مبلغ", old_amount)
    note = utility.ask_text_or_keep("توضیح", old_note)

    if amount <= 0:
        print("مبلغ باید بیشتر از صفر باشد؛ چیزی تغییر نکرد.")
        return

    try:
        updated = db.update_income(income_id, vehicle_id, date, amount, note)
    except sqlite3.IntegrityError:
        print("شماره ماشین معتبر نیست؛ چیزی تغییر نکرد.")
        return

    if updated == 0:
        print("درآمدی با این شناسه وجود نداشت.")
    else:
        print("درآمد با موفقیت ویرایش شد.")


if __name__ == "__main__":
    run()