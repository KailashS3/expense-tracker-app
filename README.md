# 💰 Expense Tracker Application

A modern **Expense Tracker Web Application** built with:

![Flask](https://img.shields.io/badge/Flask-Backend-lightgrey?logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?logo=mysql)
![Nginx](https://img.shields.io/badge/Nginx-ReverseProxy-green?logo=nginx)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker)
![Compose](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)

---

## 🚀 Features

- **Authentication**: Register, Login, Password Hashing (Flask‑Bcrypt), Session Management (Flask‑Login)  
- **Expense Management**: Add, Categorize, Describe, Date, and Track Expenses  
- **Dashboard**: View Total, Monthly, Weekly, and Selected Month Expenses  
- **Notifications**: Configure alerts (Daily, Weekly, Monthly, Yearly, Budget Limit, Custom Time)  
- **History**: Track expense logs and notification history  

---

## 🏗️ Project Architecture

```text
Browser
   ↓
Nginx
   ↓
Flask Backend
   ↓
MySQL Database

📂 Project Structure
expense-tracker-app/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── scheduler.py
│   ├── requirements.txt
│   ├── Dockerfile
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── expenses.html
│   │   ├── notifications.html
│   │   ├── settings.html
│   │   ├── login.html
│   │   └── register.html
│   │
│   └── static/
│       └── style.css
│
├── nginx/
│   └── nginx.conf
│
└── docker-compose.yml

🐳 Docker Setup

Build & Run
```
docker compose up --build
```

Run in Background
```
docker compose up -d
```

Stop
```
docker compose down
```

🔗 Access
App URL → http://localhost
Flask Backend → http://localhost:5000
MySQL Port → 3306

🔧 Common Docker Commands
Check containers → docker ps
View logs → docker compose logs -f
Restart → docker compose restart
Remove volumes → docker compose down -v

🛡️ Security Features
Password Hashing
Session Authentication
Docker Network Isolation
Environment Variables
Reverse Proxy with Nginx

📈 Future Improvements
Charts & Analytics
AI Expense Insights
SMS / Telegram Notifications
Mobile Responsive UI
PDF Export Reports
Multi-user Groups
Recurring Expenses
Category Budgeting
