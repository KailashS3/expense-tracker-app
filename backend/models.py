from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Expense(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    amount = db.Column(db.Float, nullable=False)

    category = db.Column(db.String(100))

    description = db.Column(db.String(255))

    expense_date = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )


class NotificationSetting(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    scheduler_enabled = db.Column(
        db.Boolean,
        default=False
    )

    daily_enabled = db.Column(
        db.Boolean,
        default=False
    )

    weekly_enabled = db.Column(
        db.Boolean,
        default=False
    )

    monthly_enabled = db.Column(
        db.Boolean,
        default=False
    )

    yearly_enabled = db.Column(
        db.Boolean,
        default=False
    )

    budget_limit = db.Column(
        db.Float,
        default=0
    )

    notify_time = db.Column(
        db.String(10),
        default="09:00"
    )

    notification_email = db.Column(
        db.String(255)
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )

class NotificationLog(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    message = db.Column(db.String(255))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False
    )
