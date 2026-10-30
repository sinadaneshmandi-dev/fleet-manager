import sqlite3
import db


def run():
    confirm = input("ایا مطمعنی که میخوای کل داده هات رو پاک کنی ؟ ؛ اگر مطمعنی بنویس (بله)").strip()
    if confirm == "بله":
        db.clear_all_records()
    else:
        print("خب خداروشکر مواظب باش دوباره اشتباه کلیدی رو نزنی")
        return None
    

if __name__ == "__main__":
    run()