import sqlite3
import db


def run():
    db.crear_db()
    print("Database created:",db.DB_PATH)
    
if __name__ == "__main__":
    run()