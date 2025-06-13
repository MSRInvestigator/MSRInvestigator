from flask import Flask, request, render_template, redirect, url_for, session
from passlib.hash import phpass
from models import get_db_connection
import mysql.connector

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        school = request.form["school"]

        hashed_password = phpass.hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, first_name, last_name, school) VALUES (%s, %s, %s, %s, %s)",
                           (username, hashed_password, first_name, last_name, school))
            conn.commit()
        except mysql.connector.Error as err:
            return f"Database error: {err}"
        finally:
            conn.close()

        return redirect(url_for("login"))
    return render_template("register.html")