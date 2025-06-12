import os
import mysql.connector
from passlib.hash import phpass
from dotenv import load_dotenv

load_dotenv()

def get_wp_user(username, password):
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM wp_users WHERE user_login = %s", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and phpass.verify(password, user['user_pass']):
            return user
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
    return None
