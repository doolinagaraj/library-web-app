# 📚 Library Management Web Application

## 📌 Overview
This is a **server-rendered Library Management Web Application** built using **Flask**, **JWT-based authentication**, and **SQLite3**.  
The application supports **role-based access control** with two roles: **Admin** and **Member**.

All interactions are done through **HTML pages (Jinja2 templates)**, not REST APIs, and security is enforced at the **route level**.

---

## 🛠️ Technology Stack
- Python 3.x
- Flask
- Flask-JWT-Extended (JWT stored in HTTP-only cookies)
- SQLite3 (raw SQL, no ORM)
- bcrypt (password hashing)
- Jinja2 Templates
- HTML + minimal CSS

---

## 👥 User Roles & Permissions

### 🔑 Admin
- Login to admin dashboard
- View all books (available + issued)
- Add new books
- Edit book details
- Delete books

### 👤 Member
- Login to member dashboard
- View available books
- Borrow books
- Return books

⚠️ Members cannot add, edit, or delete books.  
⚠️ Authorization is enforced on backend routes, not just UI controls.

---

## 🔐 Authentication & Authorization

- Users log in using **username and password**
- Passwords are **securely hashed using bcrypt**
- On successful login:
  - A **JWT access token** is generated
  - Token is stored in an **HTTP-only cookie**
- All routes except `/login` and `/register` require authentication
- Role-based authorization is strictly enforced on routes
- Unauthorized access results in redirect with flash message or access denial

---

## 🗄️ Database Schema

### users
| Column | Type | Description |
|------|------|-------------|
| id | INTEGER | Primary Key |
| username | TEXT | Unique |
| password | TEXT | Hashed |
| role | TEXT | admin / member |

### books
| Column | Type | Description |
|------|------|-------------|
| id | INTEGER | Primary Key |
| title | TEXT | Book title |
| author | TEXT | Author name |
| available | INTEGER | 1 = available, 0 = issued |

### borrowed_books
| Column | Type | Description |
|------|------|-------------|
| id | INTEGER | Primary Key |
| user_id | INTEGER | Borrower |
| book_id | INTEGER | Borrowed book |
| borrowed_at | TIMESTAMP | Borrow date |

---

## 🌐 Application Routes

### Public Routes
- /login
- /register
- /logout

### Admin Routes (Admin Only)
- /admin/dashboard
- /admin/books
- /admin/books/add
- /admin/books/edit/<id>
- /admin/books/delete/<id>

### Member Routes (Member Only)
- /member/dashboard
- /member/books
- /member/borrow/<book_id>
- /member/return/<book_id>

---

## ▶️ Setup Instructions

### 1. Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

Activate:
- Windows
```bash
venv\Scripts\activate
```
- Linux / Mac
```bash
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

The database (library.db) is automatically created on first run.

---

## 🔑 Admin Creation
Create an admin user via the registration page by selecting the role as **admin**.

---

## 🖥️ UI & UX
- Jinja2 template inheritance using base.html
- Flash messages for errors and success
- Role-based navigation
- Static CSS served via /static folder

---

## 🧪 Edge Cases Handled
- Unauthorized URL access
- Role mismatch access
- Borrowing unavailable books
- Duplicate usernames
- Logout session invalidation

---

## 📂 Project Structure
```
library-web-app/
├── app.py
├── auth.py
├── admin.py
├── member.py
├── database.py
├── templates/
├── static/
├── requirements.txt
└── README.md
```

---

## ✅ Expected Outcome
This project demonstrates secure authentication, role-based authorization, and a realistic Flask web application using SQLite.
