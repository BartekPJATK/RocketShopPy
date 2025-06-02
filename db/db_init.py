import sqlite3
from db.seed import seed_rockets, seed_companies
from management.helper import pretty_print

DB_NAME = "rocket_shop.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rockets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            manufacturer TEXT NOT NULL,
            range INTEGER,
            payload INTEGER,
            price INTEGER,
            available BOOLEAN DEFAULT 1
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            budget INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS company_accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id INTEGER UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            FOREIGN KEY (company_id) REFERENCES companies(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rocket_id INTEGER NOT NULL,
            company_id INTEGER NOT NULL,
            purchase_date TEXT NOT NULL,
            price INTEGER NOT NULL,
            FOREIGN KEY (rocket_id) REFERENCES rockets(id),
            FOREIGN KEY (company_id) REFERENCES companies(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    pretty_print("Database initialized!", tag="SUCCESS")
    seed_rockets()
    pretty_print("Rockets seeded!", tag="SUCCESS")
    seed_companies()
    pretty_print("Companies seeded!", tag="SUCCESS")
