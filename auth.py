import mysql.connector
from passlib.hash import phpass

def get_wp_user(username, password):
    conn = mysql.connector.connect(
        host="mysql.secureserver.net",  # Updated host for GoDaddy MySQL remote access
        user="i1816040_wp2",
        password="H.qVNOLd8O39IKmlQFa50",
        database="i1816040_wp2"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM wp_users WHERE user_login = %s", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and phpass.verify(password, user['user_pass']):
        return user
    return None
