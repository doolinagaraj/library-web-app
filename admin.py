from flask import Blueprint, render_template, redirect, flash, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import get_db

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

def admin_only():
    user = get_jwt_identity()
    if user["role"] != "admin":
        flash("Unauthorized access")
        return False
    return True

@admin_bp.route("/dashboard")
@jwt_required()
def dashboard():
    if not admin_only(): return redirect("/login")
    return render_template("admin/dashboard.html")

@admin_bp.route("/books")
@jwt_required()
def books():
    if not admin_only(): return redirect("/login")
    db = get_db()
    books = db.execute("SELECT * FROM books").fetchall()
    return render_template("admin/books.html", books=books)

@admin_bp.route("/books/add", methods=["GET", "POST"])
@jwt_required()
def add_book():
    if not admin_only(): return redirect("/login")

    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]

        db = get_db()
        db.execute(
            "INSERT INTO books (title, author, available) VALUES (?, ?, 1)",
            (title, author)
        )
        db.commit()
        flash("Book added successfully")
        return redirect("/admin/books")

    return render_template("admin/add_book.html")

@admin_bp.route("/books/edit/<int:id>", methods=["GET", "POST"])
@jwt_required()
def edit_book(id):
    if not admin_only(): return redirect("/login")
    db = get_db()

    if request.method == "POST":
        db.execute(
            "UPDATE books SET title=?, author=? WHERE id=?",
            (request.form["title"], request.form["author"], id)
        )
        db.commit()
        flash("Book updated")
        return redirect("/admin/books")

    book = db.execute("SELECT * FROM books WHERE id=?", (id,)).fetchone()
    return render_template("admin/edit_book.html", book=book)

@admin_bp.route("/books/delete/<int:id>")
@jwt_required()
def delete_book(id):
    if not admin_only(): return redirect("/login")

    db = get_db()
    db.execute("DELETE FROM books WHERE id=?", (id,))
    db.commit()
    flash("Book deleted")
    return redirect("/admin/books")
