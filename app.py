from flask import Flask, request, render_template, redirect, url_for, session
from passlib.hash import phpass, bcrypt
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="i1816040_wp2",
        password="H.qVNOLd8O39IKmlQFa50",
        database="i1816040_wp2"
    )

def get_wp_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM wp_users WHERE user_login = %s", (username,))
    user = cursor.fetchone()
    conn.close()

    if user and phpass.verify(password, user['user_pass']):
        return user
    return None

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        wp_user = get_wp_user(username, password)
        if wp_user:
            session["username"] = username
            return redirect(url_for("dashboard"))

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM intern_users WHERE username = %s", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.verify(password, user['password_hash']):
            session["username"] = username
            return redirect(url_for("dashboard"))

        return render_template("login.html", error="Invalid credentials.")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_hash = bcrypt.hash(password)
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO intern_users (username, password_hash) VALUES (%s, %s)", (username, password_hash))
            conn.commit()
            return redirect(url_for("login"))
        except mysql.connector.errors.IntegrityError:
            return render_template("register.html", error="Username already taken.")
        finally:
            conn.close()
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return f"Welcome {session['username']}! <a href='/logout'>Logout</a>"
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
