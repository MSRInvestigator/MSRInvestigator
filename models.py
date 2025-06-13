from passlib.hash import sha256_crypt
import mysql.connector
import os
from dotenv import load_dotenv
import openai

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def register_user(first_name, last_name, school, username, password):
    hashed_password = sha256_crypt.hash(password)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (first_name, last_name, school, username, password) VALUES (%s, %s, %s, %s, %s)", 
                   (first_name, last_name, school, username, hashed_password))
    conn.commit()
    conn.close()

def log_action(action):
    prompt = f"Log entry: {action}"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )