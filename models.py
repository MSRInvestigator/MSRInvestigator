
import mysql.connector
from passlib.hash import phpass

def get_wp_user(username, password):
    conn = mysql.connector.connect(
        host="msradminwp1.db.330.hostedresource.com",  # External MySQL hostname
        user="i1816040_wp2",                          # DB username
        password="H.qVNOLd8O39IKmlQFa50",             # DB password
        database="i1816040_wp2"                       # DB name
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM wp_users WHERE user_login = %s", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and phpass.verify(password, user['user_pass']):
        return user
    return None
