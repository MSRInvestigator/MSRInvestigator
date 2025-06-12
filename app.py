
from flask import Flask, render_template, request, redirect, session, url_for
from models import init_db, add_log_entry, get_logs_by_user
from gpt_assistant import summarize_hours
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "devkey")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        date = request.form["date"]
        start = request.form["start"]
        end = request.form["end"]
        task = request.form["task"]
        add_log_entry(session["username"], date, start, end, task)

    logs, total_hours = get_logs_by_user(session["username"])
    return render_template("dashboard.html", logs=logs, total_hours=total_hours)

@app.route("/admin")
def admin():
    if session.get("username") != "admin":
        return redirect(url_for("dashboard"))

    return render_template("admin.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
