
import sqlite3
from datetime import datetime

DB_PATH = "database.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            username TEXT,
            date TEXT,
            start TEXT,
            end TEXT,
            task TEXT,
            hours REAL
        )""")
        conn.commit()

def calculate_hours(start, end):
    fmt = "%H:%M"
    start_dt = datetime.strptime(start, fmt)
    end_dt = datetime.strptime(end, fmt)
    delta = (end_dt - start_dt).total_seconds() / 3600
    if delta < 0:
        delta += 24
    return round(delta, 2)

def add_log_entry(username, date, start, end, task):
    hours = calculate_hours(start, end)
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO logs (username, date, start, end, task, hours) VALUES (?, ?, ?, ?, ?, ?)",
                  (username, date, start, end, task, hours))
        conn.commit()

def get_logs_by_user(username):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT date, start, end, task, hours FROM logs WHERE username=?", (username,))
        logs = c.fetchall()
        total_hours = sum(row[4] for row in logs)
        return logs, round(total_hours, 2)
