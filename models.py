
import os
import mysql.connector

def get_logs_by_user(username):
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "i1816040_wp2"),
        password=os.getenv("DB_PASSWORD", "H.qVNOLd8O39IKmlQFa50"),
        database=os.getenv("DB_NAME", "i1816040_wp2")
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT date, start, end, task, hours FROM wp_logs WHERE username = %s", (username,))
    logs = cursor.fetchall()
    conn.close()
    total_hours = sum(entry["hours"] for entry in logs)
    return logs, total_hours

def log_hours(username, date, start, end, task, hours):
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "i1816040_wp2"),
        password=os.getenv("DB_PASSWORD", "H.qVNOLd8O39IKmlQFa50"),
        database=os.getenv("DB_NAME", "i1816040_wp2")
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO wp_logs (username, date, start, end, task, hours) VALUES (%s, %s, %s, %s, %s, %s)",
        (username, date, start, end, task, hours)
    )
    conn.commit()
    conn.close()
