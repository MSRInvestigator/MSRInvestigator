
import mysql.connector

def add_log_entry(username, start_time, end_time, total_hours):
    conn = mysql.connector.connect(
        host="localhost",
        user="i1816040_wp2",
        password="H.qVNOLd8O39IKmlQFa50",
        database="i1816040_wp2"
    )
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO wp_logs (username, start_time, end_time, total_hours)
        VALUES (%s, %s, %s, %s)
    """, (username, start_time, end_time, total_hours))
    conn.commit()
    conn.close()

def get_logs_by_user(username):
    conn = mysql.connector.connect(
        host="localhost",
        user="i1816040_wp2",
        password="H.qVNOLd8O39IKmlQFa50",
        database="i1816040_wp2"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM wp_logs WHERE username = %s", (username,))
    logs = cursor.fetchall()
    conn.close()
    return logs
