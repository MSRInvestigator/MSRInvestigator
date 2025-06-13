import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="107.180.118.250",
        user="i1816040_wp2",
        password="H.qVNOLd8O39IKmlQFa50",
        database="i1816040_wp2"
    )

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            school VARCHAR(50)
        )
    """)
    conn.commit()
    conn.close()