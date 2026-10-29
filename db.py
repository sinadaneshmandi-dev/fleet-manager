import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
DB_PATH = BASE/"fleet.db"

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def crear_db():
    conn = connect()
    try:
        conn.executescript(
             """CREATE TABLE IF NOT EXISTS vehicles (
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             plate TEXT,
             type TEXT,
             odometer_km INTEGER DEFAULT 0
         );
         
         CREATE TABLE IF NOT EXISTS expenses (
             id INTEGER PRIMARY KEY,
             vehicle_id INTEGER NOT NULL REFERENCES vehicles(id),
             date TEXT NOT NULL,
             category TEXT NOT NULL,
             amount INTEGER NOT NULL,
             note TEXT
         );
         
         CREATE TABLE IF NOT EXISTS incomes (
             id INTEGER PRIMARY KEY,
             vehicle_id INTEGER NOT NULL REFERENCES vehicles(id),
             date TEXT NOT NULL,
             amount INTEGER NOT NULL,
             note TEXT
         );"""
         )
        conn.commit()
    finally:
        conn.close()
           

def list_vehicles():
    conn = connect()
    rows = conn.execute("SELECT name, id FROM vehicles;").fetchall()
    conn.close()
    return rows

    
def add_income(vehicle_id, date, amount, note):
    conn = connect()
    try:
        cur = conn.execute(
            "INSERT INTO incomes (vehicle_id, date, amount, note) VALUES (?, ?, ?, ?)",
            (vehicle_id, date, amount, note),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()

def add_expense(vehicle_id, date, category, amount, note ):
    conn = connect()
    try:
        cur = conn.execute(
         "INSERT INTO expenses(vehicle_id, date, category, amount,note) VALUES(? , ? , ? , ? , ?)",
          (vehicle_id, date, category, amount, note),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()

def add_vehicle(name,plate,typeV,odometer_km):
    conn = connect()
    try:
        cur = conn.execute(
            "INSERT INTO vehicles(name,plate,type,odometer_km) VALUES(?,?,?,?)",
            (name,plate,typeV,odometer_km),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()

def clear_all_records():
    conn = connect()
    try:
        cur = conn.executescript(
            """DELETE FROM incomes;
                DELETE FROM expenses;
                DELETE FROM vehicles;"""
        )
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()

def list_expenses():
    conn = connect()
    rows = conn.execute("SELECT id , vehicle_id, date, category, amount FROM expenses;").fetchall()
    conn.commit()
    conn.close()
    return rows



def delete_expense(expense_id):
    conn = connect()
    try:
        cur = conn.execute(
            "DELETE FROM expenses WHERE id = ?",
            (expense_id,)
        )
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()

def list_incomes():
    conn = connect()
    rows = conn.execute("SELECT id,vehicle_id, date,amount FROM incomes; ").fetchall()
    conn.commit()
    conn.close()
    return rows

def delete_income(income_id):
    conn = connect()
    try:
        cur = conn.execute("DELETE FROM incomes WHERE id = ?",
            (income_id,))
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()

def delete_vehicle(vehicle_id):
    conn = connect()
    try:
        cur = conn.execute("DELETE FROM vehicles WHERE id = ?",
        (vehicle_id,)   )
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()

def select_expense(expense_id):
    conn = connect()
    expense = conn.execute("SELECT id , vehicle_id, date, category, amount FROM expenses WHERE id = ? " , (expense_id,)).fetchall()
    conn.close()
    return expense

def select_income(income_id):
    conn = connect()
    income = conn.execute("SELECT id,vehicle_id, date,amount FROM incomes WHERE id = ?" , (income_id,)).fetchall()
    conn.close()
    return income

def select_vehicle(vehicle_id):
    conn = connect()
    vehicle = conn.execute("SELECT name, id FROM vehicles WHERE id = ? " , (vehicle_id,)).fetchall()
    conn.close()
    return vehicle

def update_expense(expense_id,vehicle_id, date, category, amount , note):
    conn = connect()
    try:
        cur = conn.execute("UPDATE expenses SET vehicle_id = ?, date=?, category=?, amount=?, note = ? WHERE id = ?",
            (vehicle_id, date, category, amount , note, expense_id))
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()

def get_expense(expense_id):
    conn = connect()
    try:
        return conn.execute(
            "SELECT id, vehicle_id, date, category, amount, note FROM expenses WHERE id = ?",
            (expense_id,),
        ).fetchone()
    finally:
        conn.close()

def get_income(income_id):
    conn = connect()
    try:
        return conn.execute(
            "SELECT id, vehicle_id, date, amount, note FROM incomes WHERE id = ?",
            (income_id,),
        ).fetchone()
    finally:
        conn.close()


def update_income(income_id, vehicle_id, date, amount, note):
    conn = connect()
    try:
        cur = conn.execute(
            "UPDATE incomes SET vehicle_id = ?, date = ?, amount = ?, note = ? WHERE id = ?",
            (vehicle_id, date, amount, note, income_id),
        )
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()


def get_vehicle(vehicle_id):
    conn = connect()
    try:
        return conn.execute(
            "SELECT id, name, plate, type, odometer_km FROM vehicles WHERE id = ?",
            (vehicle_id,),
        ).fetchone()
    finally:
        conn.close()


def update_vehicle(vehicle_id, name, plate, typeV, odometer_km):
    conn = connect()
    try:
        cur = conn.execute(
            "UPDATE vehicles SET name = ?, plate = ?, type = ?, odometer_km = ? WHERE id = ?",
            (name, plate, typeV, odometer_km, vehicle_id),
        )
        conn.commit()
        return cur.rowcount
    finally:
        conn.close()