import os
import mysql.connector
from passlib.hash import phpass
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def create_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_pw = phpass.hash(password)
    cursor.execute("INSERT INTO wp_users (user_login, user_pass, user_email) VALUES (%s, %s, %s)",
                   (username, hashed_pw, f"{username}@example.com"))
    conn.commit()
    conn.close()

def user_exists(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ID FROM wp_users WHERE user_login = %s", (username,))
    result = cursor.fetchone()
    conn.close()
    return result is not None
