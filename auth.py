import mysql.connector
from passlib.hash import phpass

def get_wp_user(username, password):
    conn = mysql.connector.connect(
        host="your-db-host",
        user="your-db-user",
        password="your-db-password",
        database="your-wp-database"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM wp_users WHERE user_login = %s", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and phpass.verify(password, user['user_pass']):
        return user
    return None
