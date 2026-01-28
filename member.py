from flask import Blueprint, render_template, redirect, flash
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from database import get_db

member_bp = Blueprint("member", __name__, url_prefix="/member")


def member_only():
    jwt_data = get_jwt()
    if jwt_data.get("role") != "member":
        flash("Unauthorized access")
        return False
    return True


@member_bp.route("/dashboard")
@jwt_required()
def dashboard():
    if not member_only():
        return redirect("/login")
    return render_template("member/dashboard.html")


@member_bp.route("/books")
@jwt_required()
def books():
    if not member_only():
        return redirect("/login")
    db = get_db()
    books = db.execute("SELECT * FROM books WHERE available=1").fetchall()
    return render_template("member/books.html", books=books)


@member_bp.route("/borrow/<int:book_id>")
@jwt_required()
def borrow(book_id):
    if not member_only():
        return redirect("/login")

    user_id = int(get_jwt_identity())
    db = get_db()

    book = db.execute(
        "SELECT * FROM books WHERE id=? AND available=1", (book_id,)
    ).fetchone()
    if not book:
        flash("Book not available")
        return redirect("/member/books")

    db.execute(
        "INSERT INTO borrowed_books (user_id, book_id) VALUES (?, ?)",
        (user_id, book_id),
    )
    db.execute("UPDATE books SET available=0 WHERE id=?", (book_id,))
    db.commit()
    flash("Book borrowed successfully")
    return redirect("/member/books")


@member_bp.route("/return/<int:book_id>")
@jwt_required()
def return_book(book_id):
    if not member_only():
        return redirect("/login")

    user_id = int(get_jwt_identity())
    db = get_db()

    db.execute(
        "DELETE FROM borrowed_books WHERE user_id=? AND book_id=?",
        (user_id, book_id),
    )
    db.execute("UPDATE books SET available=1 WHERE id=?", (book_id,))
    db.commit()
    flash("Book returned")
    return redirect("/member/books")
