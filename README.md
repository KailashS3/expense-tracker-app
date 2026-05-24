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

```
Browser
   ↓
Nginx
   ↓
Flask Backend
   ↓
MySQL Database
```

## 📂 Project Structure
```
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
```
## 🐳 Docker Setup

Clone Setup
```
git clone https://github.com/KailashS3/expense-tracker-app.git
cd expense-tracker-app
```

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
Run in Browser
```
http://localhost:5000
```

## 🔗 Access & Setup
- App URL → http://localhost
- Flask Backend → http://localhost:5000
- MySQL Port → 3306

## 🔧 Common Docker Commands
- Check containers → docker ps
- View logs → docker compose logs -f
- Restart → docker compose restart
- Remove volumes → docker compose down -v

## 🛡️ Security Features
- Password Hashing
- Session Authentication
- Docker Network Isolation
- Environment Variables
- Reverse Proxy with Nginx

## 📈 Future Improvements
- Charts & Analytics
- AI Expense Insights
- SMS / Telegram Notifications
- Mobile Responsive UI
- PDF Export Reports
- Multi-user Groups
Recurring Expenses
Category Budgeting

## 📸 Screenshots

**Create Account**

- if user name exists then will gove error
<img width="800" height="240" alt="image" src="https://github.com/user-attachments/assets/e5979acc-b38c-4bcc-9107-f64226bfce61" />


**Login Account**

<img width="800" height="240" alt="image" src="https://github.com/user-attachments/assets/27441813-4832-4f6c-bed3-ed8c130aa5e9" />

- if email/password is incorrect then will give error
<img width="800" height="240" alt="image" src="https://github.com/user-attachments/assets/76aa6679-3b2a-4eb5-beae-2ef6de48a689" />


**Dashboard Screen**

<img width="800" height="240" alt="image" src="https://github.com/user-attachments/assets/3ffe4045-523f-4a30-a4ae-94ccdbfe03a2" />


**Expenses History Screen**

<img width="800" height="240" alt="image" src="https://github.com/user-attachments/assets/81843fe4-66cf-4bb3-9d5b-e1844d7b856b" />


**Notification Screen**

<img width="800" height="240" alt="image" src="https://github.com/user-attachments/assets/6705a8f7-6e50-420c-a71a-04718a124e17" />

**Setting Screen**
<img width="800" height="240" alt="image" src="https://github.com/user-attachments/assets/70d24a4a-1680-4018-a405-b3ca968541fe" />


