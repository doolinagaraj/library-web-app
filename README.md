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
- Unauthorized access results in:
  - Redirect with flash message OR
  - Access denial

---

## 🗄️ Database Schema

### `users`
| Column   | Type    | Description           |
|--------|---------|-----------------------|
| id     | INTEGER | Primary Key           |
| username | TEXT | Unique username       |
| password | TEXT | Hashed password       |
| role   | TEXT    | admin / member        |

### `books`
| Column   | Type    | Description            |
|--------|---------|------------------------|
| id     | INTEGER | Primary Key            |
| title  | TEXT    | Book title             |
| author | TEXT    | Author name            |
| available | INTEGER | 1 = available, 0 = issued |

### `borrowed_books`
| Column   | Type      | Description        |
|--------|-----------|--------------------|
| id     | INTEGER   | Primary Key        |
| user_id | INTEGER | Borrower ID        |
| book_id | INTEGER | Book ID            |
| borrowed_at | TIMESTAMP | Borrow date |

---

## 🌐 Application Routes

### Public Routes
- `/login` – User login
- `/register` – User registration
- `/logout` – Logout and clear JWT

### Admin Routes (Admin Only)
- `/admin/dashboard`
- `/admin/books`
- `/admin/books/add`
- `/admin/books/edit/<id>`
- `/admin/books/delete/<id>`

### Member Routes (Member Only)
- `/member/dashboard`
- `/member/books`
- `/member/borrow/<book_id>`
- `/member/return/<book_id>`

---

## ▶️ Setup Instructions

### 1️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv venv
