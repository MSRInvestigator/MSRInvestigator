from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector
import openai
from dotenv import load_dotenv
import os
from auth import verify_user
from models import register_user, log_action

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if verify_user(username, password):
            session["username"] = username
            log_action(f"User {username} logged in")
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first = request.form["first_name"]
        last = request.form["last_name"]
        school = request.form["school"]
        username = request.form["username"]
        password = request.form["password"]
        register_user(first, last, school, username, password)
        log_action(f"New user registered: {username} from {school}")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return f"Welcome {session['username']}!"
    return redirect(url_for("login"))