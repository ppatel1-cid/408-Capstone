from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from app.models import User
from app import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# -------- Register --------
@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username").strip()
        email = request.form.get("email").strip()
        password = request.form.get("password").strip()

        # Validation
        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "danger")
            return render_template("register.html")

        if User.query.filter_by(email=email).first():
            flash("Email already exists.", "danger")
            return render_template("register.html")

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created. Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


# -------- Login --------
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session["user_id"] = user.id
            session["username"] = user.username
            flash("Logged in successfully!", "success")
            return redirect(url_for("main.index"))
        else:
            flash("Invalid username or password.", "danger")

    return render_template("login.html")


# -------- Logout --------
@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out.", "info")
    return redirect(url_for("main.index"))
