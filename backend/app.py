from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user
)

from config import Config
from models import db, User, Expense, NotificationSetting,NotificationLog
from datetime import datetime, timedelta
from sqlalchemy import extract,func

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():

    message = ""
    if request.method == "POST":

        username = request.form["username"]

        email = request.form["email"]

        password = request.form["password"]

        confirm_password = request.form["confirm_password"]

        existing_user = User.query.filter(
            (User.email == email) |
            (User.username == username)
        ).first()

        if existing_user:

            message = "User already exists"

            return render_template(
                "register.html",
                message=message
            )

        if password != confirm_password:

            message = "Passwords do not match"

            return render_template(
                "register.html",
                message=message
            )

        hashed_password = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(user)

        db.session.commit()

        return redirect(url_for("login"))

    return render_template(
        "register.html",
        message=message
    )

@app.route("/login", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(
            user.password,
            password
        ):

            login_user(user)

            return redirect(url_for("dashboard"))

        else:

            message = "Invalid email or password"

    return render_template(
        "login.html",
        message=message
    )


@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    if request.method == "POST":

        amount = request.form["amount"]

        category = request.form["category"]

        description = request.form[
            "description"
        ]

        expense_date = request.form[
            "expense_date"
        ]

        expense = Expense(
            amount=amount,
            category=category,
            description=description,
            expense_date=datetime.strptime(
                expense_date,
                "%Y-%m-%d"
            ),
            user_id=current_user.id
        )

        db.session.add(expense)

        db.session.commit()

        notification = NotificationLog(
            user_id=current_user.id,
            message=(
                f"Expense Added ₹{amount}"
            )
        )

        db.session.add(notification)

        db.session.commit()

        return redirect(
            url_for("dashboard")
        )

    selected_month = request.args.get(
        "month",
        datetime.now().strftime("%Y-%m")
    )

    selected_year = int(
        selected_month.split("-")[0]
    )

    selected_month_number = int(
        selected_month.split("-")[1]
    )

    today = datetime.now()

    week_ago = today - timedelta(days=7)

    expenses = Expense.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Expense.expense_date.desc()
    ).all()

    total_expense = db.session.query(
        func.sum(Expense.amount)
    ).filter(
        Expense.user_id == current_user.id
    ).scalar() or 0

    selected_month_total = db.session.query(
        func.sum(Expense.amount)
    ).filter(
        Expense.user_id == current_user.id,
        extract(
            'year',
            Expense.expense_date
        ) == selected_year,
        extract(
            'month',
            Expense.expense_date
        ) == selected_month_number
    ).scalar() or 0

    current_month = today.strftime("%Y-%m")

    if selected_month == current_month:

        monthly_total = db.session.query(
            func.sum(Expense.amount)
        ).filter(
            Expense.user_id == current_user.id,
            extract(
                'year',
                Expense.expense_date
            ) == today.year,
            extract(
                'month',
                Expense.expense_date
            ) == today.month
        ).scalar() or 0

        weekly_total = db.session.query(
            func.sum(Expense.amount)
        ).filter(
            Expense.user_id == current_user.id,
            Expense.expense_date >= week_ago
        ).scalar() or 0

    else:
        monthly_total = 0
        weekly_total = 0
    
    formatted_selected_month = datetime.strptime(
        selected_month,
        "%Y-%m"
    ).strftime("%B %Y")   
    
    notifications = NotificationLog.query.filter_by(
        user_id=current_user.id
    ).order_by(
        NotificationLog.created_at.desc()
    ).all()

    return render_template(
        "dashboard.html",
        expenses=expenses,
        total_expense=total_expense,
        selected_month_total=selected_month_total,
        monthly_total=monthly_total,
        weekly_total=weekly_total,
        notifications=notifications,
        selected_month=selected_month,
        formatted_selected_month=formatted_selected_month
    )

@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():

    setting = NotificationSetting.query.filter_by(
        user_id=current_user.id
    ).first()

    if not setting:

        setting = NotificationSetting(
            user_id=current_user.id
        )

        db.session.add(setting)

        db.session.commit()

    if request.method == "POST":

        setting.scheduler_enabled = (
            "scheduler_enabled" in request.form
        )

        setting.daily_enabled = (
            "daily_enabled" in request.form
        )

        setting.weekly_enabled = (
            "weekly_enabled" in request.form
        )

        setting.monthly_enabled = (
            "monthly_enabled" in request.form
        )

        setting.yearly_enabled = (
            "yearly_enabled" in request.form
        )

        setting.budget_limit = request.form[
            "budget_limit"
        ]

        #setting.notify_time = request.form[
        #     "notify_time"
        #]

        #setting.notification_email = request.form[
         #   "notification_email"
        #]

        db.session.commit()

    return render_template(
        "settings.html",
        setting=setting
    )

@app.route("/expenses")
@login_required
def expenses():

    expenses = Expense.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Expense.expense_date.desc()
    ).all()

    return render_template(
        "expenses.html",
        expenses=expenses
    )

@app.route("/notifications")
@login_required
def notifications():

    notifications = NotificationLog.query.filter_by(
        user_id=current_user.id
    ).order_by(
        NotificationLog.created_at.desc()
    ).all()

    return render_template(
        "notifications.html",
        notifications=notifications
    )

@app.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(url_for("login"))


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
