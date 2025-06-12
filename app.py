
from flask import Flask, render_template, request, redirect, url_for, session
from models import add_log_entry, get_logs_by_user
from auth import get_wp_user

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = get_wp_user(username, password)
        if user:
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials.")
    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    username = session["username"]

    if request.method == "POST":
        description = request.form["description"]
        add_log_entry(username, description)

    logs = get_logs_by_user(username)
    return render_template("logs.html", username=username, logs=logs)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
