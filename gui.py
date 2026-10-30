import sqlite3
import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

import db
import report_profit


TABLES = {
    "vehicles": {
        "title": "ماشین‌ها",
        "columns": ("id", "name", "plate", "type", "odometer_km"),
        "headings": ("شناسه", "نام", "پلاک", "نوع", "کیلومتر"),
    },
    "expenses": {
        "title": "هزینه‌ها",
        "columns": ("id", "vehicle_id", "date", "category", "amount"),
        "headings": ("شناسه", "ماشین", "تاریخ", "دسته", "مبلغ"),
    },
    "incomes": {
        "title": "درآمدها",
        "columns": ("id", "vehicle_id", "date", "amount"),
        "headings": ("شناسه", "ماشین", "تاریخ", "مبلغ"),
    },
}


def configure_style(root):
    style = ttk.Style(root)

    if "clam" in style.theme_names():
        style.theme_use("clam")

    style.configure("TNotebook", background="#f2f5f8", borderwidth=0)
    style.configure(
        "TNotebook.Tab",
        padding=(18, 9),
        font=("Segoe UI", 10),
    )
    style.configure(
        "Treeview",
        rowheight=30,
        font=("Segoe UI", 10),
        background="white",
    )
    style.configure(
        "Treeview.Heading",
        font=("Segoe UI", 10, "bold"),
        background="#dfe8f1",
    )
    style.configure(
        "TButton",
        padding=(12, 7),
        font=("Segoe UI", 9),
    )
    style.configure("TLabel", font=("Segoe UI", 10))


def get_rows(kind):
    functions = {
        "vehicles": db.list_vehicles,
        "expenses": db.list_expenses,
        "incomes": db.list_incomes,
    }
    return functions[kind]()


def load_table(tree, kind):
    tree.delete(*tree.get_children())

    for row in get_rows(kind):
        values = list(row)

        amount_index = {
            "expenses": 4,
            "incomes": 3,
        }.get(kind)

        if amount_index is not None:
            values[amount_index] = f"{values[amount_index]:,}"

        tree.insert("", "end", values=values)


def refresh_all(trees):
    for kind, tree in trees.items():
        load_table(tree, kind)


def open_form(root, trees, kind, record=None):
    vehicle_rows = db.list_vehicles()
    vehicles = {
        f"{row[1]} ({row[0]})": row[0]
        for row in vehicle_rows
    }

    if kind in ("expenses", "incomes") and not vehicles:
        messagebox.showinfo("ماشین", "اول یک ماشین ثبت کنید.", parent=root)
        return

    fields = {
        "vehicles": [
            ("name", "نام ماشین"),
            ("plate", "پلاک"),
            ("type", "نوع ماشین"),
            ("odometer_km", "کیلومتر"),
        ],
        "expenses": [
            ("vehicle_id", "ماشین"),
            ("date", "تاریخ YYYY-MM-DD"),
            ("category", "دسته"),
            ("amount", "مبلغ"),
            ("note", "توضیح"),
        ],
        "incomes": [
            ("vehicle_id", "ماشین"),
            ("date", "تاریخ YYYY-MM-DD"),
            ("amount", "مبلغ"),
            ("note", "توضیح"),
        ],
    }[kind]

    keys = {
        "vehicles": ("name", "plate", "type", "odometer_km"),
        "expenses": ("vehicle_id", "date", "category", "amount", "note"),
        "incomes": ("vehicle_id", "date", "amount", "note"),
    }[kind]

    values = dict(zip(keys, record[1:])) if record else {}

    if not record and kind in ("expenses", "incomes"):
        values["date"] = datetime.now().strftime("%Y-%m-%d")

    win = tk.Toplevel(root)
    win.title(("ویرایش " if record else "افزودن ") + TABLES[kind]["title"])
    win.transient(root)
    win.resizable(False, False)

    form = ttk.Frame(win, padding=18)
    form.grid(sticky="nsew")
    widgets = {}

    for row_index, (key, label) in enumerate(fields):
        ttk.Label(form, text=label).grid(
            row=row_index,
            column=1,
            sticky="e",
            padx=(12, 0),
            pady=6,
        )

        if key == "vehicle_id":
            widget = ttk.Combobox(
                form,
                values=list(vehicles),
                state="readonly",
                width=30,
            )

            old_id = values.get(key)
            for label_text, vehicle_id in vehicles.items():
                if vehicle_id == old_id:
                    widget.set(label_text)
                    break
        else:
            widget = ttk.Entry(form, width=33, justify="right")
            old_value = values.get(key)

            if old_value is not None:
                widget.insert(0, str(old_value))

        widget.grid(row=row_index, column=0, pady=6)
        widgets[key] = widget

    def save():
        data = {}

        for key, widget in widgets.items():
            raw = widget.get().strip()

            if key == "vehicle_id":
                data[key] = vehicles.get(raw)
                if data[key] is None:
                    messagebox.showerror(
                        "خطا",
                        "یک ماشین معتبر انتخاب کنید.",
                        parent=win,
                    )
                    return
            else:
                data[key] = raw

        try:
            if kind in ("expenses", "incomes"):
                data["date"] = datetime.strptime(
                    data["date"],
                    "%Y-%m-%d",
                ).strftime("%Y-%m-%d")

                amount = int(data["amount"].replace(",", ""))
                if amount <= 0:
                    raise ValueError

                data["amount"] = amount
                data["note"] = data["note"] or None

                if kind == "expenses" and not data["category"]:
                    messagebox.showerror(
                        "خطا",
                        "دسته‌ی هزینه را وارد کنید.",
                        parent=win,
                    )
                    return
            else:
                if not data["name"]:
                    messagebox.showerror(
                        "خطا",
                        "نام ماشین را وارد کنید.",
                        parent=win,
                    )
                    return

                data["odometer_km"] = int(data["odometer_km"] or "0")
                if data["odometer_km"] < 0:
                    raise ValueError

                data["plate"] = data["plate"] or None
                data["type"] = data["type"] or None

        except ValueError:
            messagebox.showerror(
                "خطا",
                "تاریخ، مبلغ یا کیلومتر معتبر نیست.",
                parent=win,
            )
            return

        try:
            if kind == "vehicles":
                args = (
                    data["name"],
                    data["plate"],
                    data["type"],
                    data["odometer_km"],
                )
                if record:
                    result = db.update_vehicle(record[0], *args)
                else:
                    result = db.add_vehicle(*args)

            elif kind == "expenses":
                args = (
                    data["vehicle_id"],
                    data["date"],
                    data["category"],
                    data["amount"],
                    data["note"],
                )
                if record:
                    result = db.update_expense(record[0], *args)
                else:
                    result = db.add_expense(*args)

            else:
                args = (
                    data["vehicle_id"],
                    data["date"],
                    data["amount"],
                    data["note"],
                )
                if record:
                    result = db.update_income(record[0], *args)
                else:
                    result = db.add_income(*args)

            if record and result == 0:
                messagebox.showerror(
                    "خطا",
                    "این ردیف دیگر وجود ندارد.",
                    parent=win,
                )
                refresh_all(trees)
                return

        except sqlite3.IntegrityError:
            messagebox.showerror(
                "خطا",
                "این تغییر با داده‌های وابسته سازگار نیست.",
                parent=win,
            )
            return
        except sqlite3.Error as error:
            messagebox.showerror(
                "خطای پایگاه داده",
                str(error),
                parent=win,
            )
            return

        refresh_all(trees)
        win.destroy()

    buttons = ttk.Frame(form)
    buttons.grid(row=len(fields), column=0, columnspan=2, pady=(14, 0))

    ttk.Button(buttons, text="ذخیره", command=save).pack(side="left", padx=5)
    ttk.Button(buttons, text="لغو", command=win.destroy).pack(side="left", padx=5)

    win.grab_set()


def edit_selected(root, trees, kind):
    tree = trees[kind]
    selected = tree.selection()

    if not selected:
        messagebox.showinfo("ویرایش", "اول یک ردیف انتخاب کنید.", parent=root)
        return

    record_id = tree.item(selected[0], "values")[0]

    selectors = {
        "vehicles": db.select_vehicle,
        "expenses": db.select_expense,
        "incomes": db.select_income,
    }

    record = selectors[kind](record_id)

    if record is None:
        messagebox.showerror("خطا", "این ردیف پیدا نشد.", parent=root)
        refresh_all(trees)
        return

    open_form(root, trees, kind, record)


def delete_selected(root, trees, kind):
    tree = trees[kind]
    selected = tree.selection()

    if not selected:
        messagebox.showinfo("حذف", "اول یک ردیف انتخاب کنید.", parent=root)
        return

    record_id = tree.item(selected[0], "values")[0]
    title = TABLES[kind]["title"]

    confirmed = messagebox.askyesno(
        "تأیید حذف",
        f"{title} با شناسه‌ی {record_id} حذف شود؟",
        parent=root,
    )

    if not confirmed:
        return

    deleters = {
        "vehicles": db.delete_vehicle,
        "expenses": db.delete_expense,
        "incomes": db.delete_income,
    }

    try:
        deleted = deleters[kind](record_id)
    except sqlite3.IntegrityError:
        messagebox.showerror(
            "حذف نشد",
            "برای این ماشین درآمد یا هزینه ثبت شده؛ اول آن‌ها را بررسی کنید.",
            parent=root,
        )
        return

    if deleted == 0:
        messagebox.showinfo("حذف", "این ردیف دیگر وجود ندارد.", parent=root)

    refresh_all(trees)


def build_data_tab(root, notebook, trees, kind):
    config = TABLES[kind]
    page = ttk.Frame(notebook, padding=10)
    notebook.add(page, text=config["title"])

    tree = ttk.Treeview(
        page,
        columns=config["columns"],
        show="headings",
        selectmode="browse",
    )

    for column, heading in zip(config["columns"], config["headings"]):
        tree.heading(column, text=heading)
        tree.column(column, width=135, anchor="center")

    tree.pack(fill="both", expand=True)
    trees[kind] = tree

    buttons = ttk.Frame(page)
    buttons.pack(pady=(10, 0))

    ttk.Button(
        buttons,
        text="افزودن",
        command=lambda: open_form(root, trees, kind),
    ).pack(side="left", padx=4)

    ttk.Button(
        buttons,
        text="ویرایش",
        command=lambda: edit_selected(root, trees, kind),
    ).pack(side="left", padx=4)

    ttk.Button(
        buttons,
        text="حذف",
        command=lambda: delete_selected(root, trees, kind),
    ).pack(side="left", padx=4)

    ttk.Button(
        buttons,
        text="تازه‌سازی",
        command=lambda: load_table(tree, kind),
    ).pack(side="left", padx=4)

    tree.bind(
        "<Double-1>",
        lambda event: edit_selected(root, trees, kind),
    )

    load_table(tree, kind)


def build_profit_tab(notebook):
    page = ttk.Frame(notebook, padding=10)
    notebook.add(page, text="گزارش سود")

    columns = ("name", "income", "expense", "profit")
    headings = ("ماشین", "درآمد", "هزینه", "سود")

    tree = ttk.Treeview(page, columns=columns, show="headings")

    for column, heading in zip(columns, headings):
        tree.heading(column, text=heading)
        tree.column(column, width=170, anchor="center")

    tree.pack(fill="both", expand=True)

    def refresh_report():
        tree.delete(*tree.get_children())

        try:
            rows = report_profit.get_report_profit()
            for name, income, expense, profit in rows:
                tree.insert(
                    "",
                    "end",
                    values=(
                        name,
                        f"{income:,}",
                        f"{expense:,}",
                        f"{profit:,}",
                    ),
                )
        except (sqlite3.Error, OSError) as error:
            messagebox.showerror(
                "خطای گزارش",
                f"گزارش بارگذاری نشد:\n{error}",
                parent=page,
            )

    ttk.Button(
        page,
        text="تازه‌سازی گزارش",
        command=refresh_report,
    ).pack(pady=(10, 0))

    refresh_report()


def main():
    db.crear_db()

    root = tk.Tk()
    root.title("مدیریت ناوگان")
    root.geometry("950x560")

    configure_style(root)

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=12, pady=12)

    trees = {}

    for kind in ("vehicles", "expenses", "incomes"):
        build_data_tab(root, notebook, trees, kind)

    build_profit_tab(notebook)

    return root


if __name__ == "__main__":
    main().mainloop()