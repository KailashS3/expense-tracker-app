# 📊 Database Schema — Expense Tracker Application

This document describes the database tables used in the Expense Tracker Application.

---

## 🧑 Users Table

Stores user information.

| Column   | Type    | Description              |
|----------|---------|--------------------------|
| id       | Integer | Primary key              |
| username | String  | Unique username          |
| email    | String  | User email address       |
| password | String  | Hashed password          |

---

## 💵 Expense Table

Stores expense records.

| Column       | Type    | Description                  |
|--------------|---------|------------------------------|
| id           | Integer | Primary key                  |
| amount       | Float   | Expense amount               |
| category     | String  | Expense category             |
| description  | String  | Expense description          |
| expense_date | Date    | Date of expense              |
| user_id      | Integer | Foreign key → users.id       |

---

## 🔔 Notification Settings Table

Stores user notification preferences.

| Column            | Type    | Description                  |
|-------------------|---------|------------------------------|
| id                | Integer | Primary key                  |
| scheduler_enabled | Boolean | Enable/disable scheduler     |
| daily_enabled     | Boolean | Daily alerts                 |
| weekly_enabled    | Boolean | Weekly alerts                |
| monthly_enabled   | Boolean | Monthly alerts               |
| yearly_enabled    | Boolean | Yearly alerts                |
| budget_limit      | Float   | Budget limit for alerts      |
| notify_time       | String  | Preferred notification time  |
| user_id           | Integer | Foreign key → users.id       |

---

## 📜 Notification Log Table

Stores notification history.

| Column     | Type     | Description                  |
|------------|----------|------------------------------|
| id         | Integer  | Primary key                  |
| message    | String   | Notification message         |
| created_at | DateTime | Timestamp of notification    |
| user_id    | Integer  | Foreign key → users.id       |

---

## 🔗 Relationships

- **users → expense**: One user can have many expenses.  
- **users → notification_setting**: One user has one notification setting record.  
- **users → notification_log**: One user can have many notification logs.  

---

## ⚙️ Notes

- Passwords are stored securely using **Flask‑Bcrypt hashing**.  
- Foreign keys ensure relational integrity between tables.  
- Designed for scalability with Dockerized MySQL.  

