import os
import sqlite3
from functools import wraps

DB_PATH = os.path.join(os.path.dirname(__file__), "rocket_shop.db")

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def with_db(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with connect() as conn:
            return func(conn, *args, **kwargs)
    return wrapper
