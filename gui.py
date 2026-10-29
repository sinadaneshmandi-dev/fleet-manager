import sqlite3
import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox
import db

COLUMNS = ("id", "vehicle_id", "date", "category", "amount")
HEADINGS = {
    "id": "شناسه",
    "vehicle_id": "ماشین",
    "date": "تاریخ",
    "category": "دسته",
    "amount": "مبلغ",
}


def load_expenses(tree):
    for item in tree.get_children():
        tree.delete(item)
    for exp_id, vehicle_id, date, category, amount in db.list_expenses():
        tree.insert("", "end", values=(exp_id, vehicle_id, date, category, f"{amount:,}"))


def check_expense(vehicle_choice, vehicles, date_text, category, amount_text, note):
    vehicle_id = vehicles.get(vehicle_choice)
    if vehicle_id is None:
        return None, "یک ماشین انتخاب کنید."

    try:
        date_text = datetime.strptime(date_text.strip(), "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        return None, "تاریخ باید به شکل YYYY-MM-DD باشد (مثلاً 2026-10-29)."

    category = category.strip()
    if not category:
        return None, "دسته را وارد کنید."

    try:
        amount = int(amount_text.replace(",", "").strip())
    except ValueError:
        return None, "مبلغ باید یک عدد باشد."
    if amount <= 0:
        return None, "مبلغ باید بیشتر از صفر باشد."

    note = note.strip() or None
    return (vehicle_id, date_text, category, amount, note), None


def open_expense_form(root, tree, expense=None):
    vehicles = {f"{name} ({vid})": vid for name, vid in db.list_vehicles()}
    if not vehicles:
        messagebox.showinfo("ماشین", "اول باید حداقل یک ماشین ثبت شود.")
        return

    win = tk.Toplevel(root)
    win.title("ویرایش هزینه" if expense else "هزینه‌ی جدید")
    win.transient(root)
    win.grab_set()

    form = ttk.Frame(win, padding=15)
    form.pack()

    labels = ["ماشین", "تاریخ (YYYY-MM-DD)", "دسته", "مبلغ", "توضیح"]
    for row_number, text in enumerate(labels):
        ttk.Label(form, text=text).grid(row=row_number, column=1, sticky="e", padx=(10, 0), pady=5)

    vehicle_box = ttk.Combobox(form, values=list(vehicles), state="readonly", width=30)
    date_entry = ttk.Entry(form, width=33, justify="right")
    category_box = ttk.Combobox(form, values=["سوخت", "تعمیر"], width=30)
    amount_entry = ttk.Entry(form, width=33, justify="right")
    note_entry = ttk.Entry(form, width=33, justify="right")

    for row_number, widget in enumerate([vehicle_box, date_entry, category_box, amount_entry, note_entry]):
        widget.grid(row=row_number, column=0, pady=5)

    if expense is None:
        date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))
    else:
        _, old_vehicle_id, old_date, old_category, old_amount, old_note = expense
        for label, vid in vehicles.items():
            if vid == old_vehicle_id:
                vehicle_box.set(label)
        date_entry.insert(0, old_date)
        category_box.set(old_category)
        amount_entry.insert(0, str(old_amount))
        note_entry.insert(0, old_note or "")

    def save():
        values, error = check_expense(
            vehicle_box.get(), vehicles, date_entry.get(),
            category_box.get(), amount_entry.get(), note_entry.get(),
        )
        if error:
            messagebox.showerror("خطا", error, parent=win)
            return
        try:
            if expense is None:
                db.add_expense(*values)
            elif db.update_expense(expense[0], *values) == 0:
                messagebox.showerror("خطا", "این هزینه دیگر وجود ندارد.", parent=win)
                return
        except sqlite3.IntegrityError:
            messagebox.showerror("خطا", "ماشین انتخاب‌شده معتبر نیست.", parent=win)
            return
        load_expenses(tree)
        win.destroy()

    buttons = ttk.Frame(win)
    buttons.pack(pady=(0, 15))
    ttk.Button(buttons, text="ذخیره", command=save).pack(side="left", padx=5)
    ttk.Button(buttons, text="انصراف", command=win.destroy).pack(side="left", padx=5)


def delete_selected(tree):
    selected = tree.selection()
    if not selected:
        messagebox.showinfo("حذف", "اول یک ردیف را انتخاب کنید.")
        return
    expense_id = tree.item(selected[0])["values"][0]
    if not messagebox.askyesno("حذف", f"هزینه‌ی شماره {expense_id} حذف شود؟"):
        return
    deleted = db.delete_expense(expense_id)
    if deleted == 0:
        messagebox.showerror("خطا", "این هزینه دیگر وجود ندارد.")
    load_expenses(tree)

def edit_selected(root, tree):
    selected = tree.selection()
    if not selected:
        messagebox.showinfo("ویرایش", "اول یک ردیف را انتخاب کنید.")
        return
    expense_id = tree.item(selected[0])["values"][0]
    expense = db.get_expense(expense_id)
    if expense is None:
        messagebox.showerror("خطا", "این هزینه دیگر وجود ندارد.")
        load_expenses(tree)
        return
    open_expense_form(root, tree, expense)


def on_double_click(event, root, tree):
    if tree.identify_region(event.x, event.y) == "cell":
        edit_selected(root, tree)

def build_expenses_tab(root, notebook):
    page = ttk.Frame(notebook)
    notebook.add(page, text="هزینه‌ها")

    tree = ttk.Treeview(page, columns=COLUMNS, show="headings")
    for col in COLUMNS:
        tree.heading(col, text=HEADINGS[col])
        tree.column(col, width=120, anchor="center")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    buttons = ttk.Frame(page)
    buttons.pack(pady=(0, 10))
    ttk.Button(buttons, text="افزودن", command=lambda: open_expense_form(root, tree)).pack(side="left", padx=5)
    ttk.Button(buttons, text="ویرایش", command=lambda: edit_selected(root, tree)).pack(side="left", padx=5)
    ttk.Button(buttons, text="حذف", command=lambda: delete_selected(tree)).pack(side="left", padx=5)
    ttk.Button(buttons, text="تازه‌سازی", command=lambda: load_expenses(tree)).pack(side="left", padx=5)
    tree.bind("<Double-1>", lambda event: on_double_click(event, root, tree))
    load_expenses(tree)
    return tree

def main():
    db.crear_db()

    root = tk.Tk()
    root.title("مدیریت ناوگان")
    root.geometry("800x450")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    build_expenses_tab(root, notebook)

    return root


if __name__ == "__main__":
    root = main()
    root.mainloop()