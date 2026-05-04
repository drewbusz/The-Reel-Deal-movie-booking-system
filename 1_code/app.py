import os
import random
import string
import mysql.connector
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, session, url_for, flash

app = Flask(__name__)
app.secret_key = "demo-secret-key"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password123",
    "database": "reel_deal"
}

UPLOAD_FOLDER = os.path.join("static", "images")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "svg"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def get_db():
    return mysql.connector.connect(**DB_CONFIG)


def generate_ticket_code():
    return "TCK-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def create_seats_for_showtime(cursor, showtime_id):
    rows = ["A", "B", "C", "D"]
    numbers = range(1, 9)

    for row in rows:
        for number in numbers:
            seat_label = f"{row}{number}"
            cursor.execute("""
                INSERT INTO seats (showtime_id, seat_label, status)
                VALUES (%s, %s, 'available')
            """, (showtime_id, seat_label))


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cursor.fetchone()
        db.close()

        if user:
            session["user_id"] = user["id"]
            session["role"] = user["role"]

            if user["role"] == "staff":
                return redirect(url_for("validate_ticket"))

            return redirect(url_for("movies"))

        flash("Invalid email or password.")

    return render_template("login.html")


@app.route("/movies")
def movies():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if session.get("role") != "customer":
        return redirect(url_for("validate_ticket"))

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT movies.id AS movie_id,
               movies.title,
               movies.description,
               movies.poster_path,
               showtimes.id AS showtime_id,
               showtimes.show_time,
               showtimes.auditorium
        FROM movies
        JOIN showtimes ON movies.id = showtimes.movie_id
        ORDER BY movies.id, showtimes.id
    """)

    rows = cursor.fetchall()
    db.close()

    grouped_movies = {}

    for row in rows:
        movie_id = row["movie_id"]

        if movie_id not in grouped_movies:
            grouped_movies[movie_id] = {
                "title": row["title"],
                "description": row["description"],
                "poster_path": row["poster_path"],
                "showtimes": []
            }

        grouped_movies[movie_id]["showtimes"].append({
            "showtime_id": row["showtime_id"],
            "show_time": row["show_time"],
            "auditorium": row["auditorium"]
        })

    return render_template("movies.html", movies=grouped_movies.values())


@app.route("/seats/<int:showtime_id>")
def seats(showtime_id):
    if "user_id" not in session:
        return redirect(url_for("login"))

    if session.get("role") != "customer":
        return redirect(url_for("validate_ticket"))

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT movies.title,
               showtimes.show_time,
               showtimes.auditorium
        FROM showtimes
        JOIN movies ON showtimes.movie_id = movies.id
        WHERE showtimes.id=%s
    """, (showtime_id,))

    showtime = cursor.fetchone()

    if not showtime:
        db.close()
        flash("Showtime not found.")
        return redirect(url_for("movies"))

    cursor.execute("""
        SELECT *
        FROM seats
        WHERE showtime_id=%s
        ORDER BY seat_label
    """, (showtime_id,))

    seat_rows = cursor.fetchall()
    db.close()

    seats_by_row = {
        "A": [],
        "B": [],
        "C": [],
        "D": []
    }

    for seat in seat_rows:
        row_letter = seat["seat_label"][0]
        seats_by_row[row_letter].append(seat)

    return render_template(
        "seats.html",
        showtime=showtime,
        seats_by_row=seats_by_row,
        showtime_id=showtime_id
    )


@app.route("/book", methods=["POST"])
def book():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if session.get("role") != "customer":
        return redirect(url_for("validate_ticket"))

    showtime_id = request.form["showtime_id"]
    selected_seats = request.form.getlist("seat_labels")

    if not selected_seats:
        flash("Please select at least one seat.")
        return redirect(url_for("seats", showtime_id=showtime_id))

    db = get_db()
    cursor = db.cursor(dictionary=True)

    placeholders = ", ".join(["%s"] * len(selected_seats))

    cursor.execute(f"""
        SELECT seat_label, status
        FROM seats
        WHERE showtime_id=%s
        AND seat_label IN ({placeholders})
    """, [showtime_id] + selected_seats)

    seats = cursor.fetchall()

    if len(seats) != len(selected_seats):
        db.close()
        flash("One or more selected seats could not be found.")
        return redirect(url_for("seats", showtime_id=showtime_id))

    unavailable_seats = []

    for seat in seats:
        if seat["status"] != "available":
            unavailable_seats.append(seat["seat_label"])

    if unavailable_seats:
        db.close()
        flash("One or more selected seats are already reserved.")
        return redirect(url_for("seats", showtime_id=showtime_id))

    ticket_code = generate_ticket_code()

    for seat_label in selected_seats:
        cursor.execute("""
            INSERT INTO bookings (user_id, showtime_id, seat_label, ticket_code)
            VALUES (%s, %s, %s, %s)
        """, (session["user_id"], showtime_id, seat_label, ticket_code))

        cursor.execute("""
            UPDATE seats
            SET status='reserved'
            WHERE showtime_id=%s
            AND seat_label=%s
        """, (showtime_id, seat_label))

    db.commit()
    db.close()

    return redirect(url_for("confirmation", ticket_code=ticket_code))


@app.route("/confirmation/<ticket_code>")
def confirmation(ticket_code):
    if "user_id" not in session:
        return redirect(url_for("login"))

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT bookings.ticket_code,
               bookings.seat_label,
               bookings.ticket_status,
               bookings.booked_at,
               movies.title,
               showtimes.show_time,
               showtimes.auditorium
        FROM bookings
        JOIN showtimes ON bookings.showtime_id = showtimes.id
        JOIN movies ON showtimes.movie_id = movies.id
        WHERE bookings.ticket_code=%s
        ORDER BY bookings.seat_label
    """, (ticket_code,))

    bookings = cursor.fetchall()
    db.close()

    if not bookings:
        flash("Booking not found.")
        return redirect(url_for("movies"))

    order = {
        "ticket_code": ticket_code,
        "title": bookings[0]["title"],
        "show_time": bookings[0]["show_time"],
        "auditorium": bookings[0]["auditorium"],
        "ticket_status": bookings[0]["ticket_status"],
        "booked_at": bookings[0]["booked_at"],
        "seats": [booking["seat_label"] for booking in bookings],
        "ticket_count": len(bookings)
    }

    return render_template("confirmation.html", order=order)


@app.route("/validate-ticket", methods=["GET", "POST"])
def validate_ticket():
    if "user_id" not in session or session.get("role") != "staff":
        return redirect(url_for("login"))

    result = None

    if request.method == "POST":
        ticket_code = request.form["ticket_code"].strip().upper()

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute("""
            SELECT bookings.ticket_code,
                   bookings.seat_label,
                   bookings.ticket_status,
                   movies.title,
                   showtimes.show_time,
                   showtimes.auditorium
            FROM bookings
            JOIN showtimes ON bookings.showtime_id = showtimes.id
            JOIN movies ON showtimes.movie_id = movies.id
            WHERE bookings.ticket_code=%s
            ORDER BY bookings.seat_label
        """, (ticket_code,))

        bookings = cursor.fetchall()

        if bookings:
            ticket_status = bookings[0]["ticket_status"]

            order = {
                "ticket_code": ticket_code,
                "title": bookings[0]["title"],
                "show_time": bookings[0]["show_time"],
                "auditorium": bookings[0]["auditorium"],
                "ticket_status": ticket_status,
                "seats": [booking["seat_label"] for booking in bookings],
                "ticket_count": len(bookings)
            }

            if ticket_status == "active":
                cursor.execute(
                    "UPDATE bookings SET ticket_status='used' WHERE ticket_code=%s",
                    (ticket_code,)
                )

                db.commit()

                result = {
                    "message": "Valid ticket. Entry allowed.",
                    "order": order
                }

            else:
                result = {
                    "message": "Ticket has already been used.",
                    "order": order
                }

        else:
            result = {
                "message": "Invalid ticket.",
                "order": None
            }

        db.close()

    return render_template("validate_ticket.html", result=result)


@app.route("/staff-bookings")
def staff_bookings():
    if "user_id" not in session or session.get("role") != "staff":
        return redirect(url_for("login"))

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT bookings.ticket_code,
               GROUP_CONCAT(bookings.seat_label ORDER BY bookings.seat_label SEPARATOR ', ') AS seats,
               COUNT(bookings.id) AS ticket_count,
               MIN(bookings.ticket_status) AS ticket_status,
               MIN(bookings.booked_at) AS booked_at,
               movies.title,
               showtimes.show_time,
               showtimes.auditorium
        FROM bookings
        JOIN showtimes ON bookings.showtime_id = showtimes.id
        JOIN movies ON showtimes.movie_id = movies.id
        GROUP BY bookings.ticket_code,
                 movies.title,
                 showtimes.show_time,
                 showtimes.auditorium
        ORDER BY booked_at DESC
    """)

    bookings = cursor.fetchall()
    db.close()

    return render_template("staff_bookings.html", bookings=bookings)


@app.route("/manage-movies", methods=["GET", "POST"])
def manage_movies():
    if "user_id" not in session or session.get("role") != "staff":
        return redirect(url_for("login"))

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    if request.method == "POST":
        title = request.form["title"].strip()
        description = request.form["description"].strip()
        show_time = request.form["show_time"].strip()
        auditorium = request.form["auditorium"].strip()
        poster = request.files.get("poster")

        poster_path = "images/default_poster.svg"

        if poster and poster.filename:
            if allowed_file(poster.filename):
                filename = secure_filename(poster.filename)
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                poster.save(save_path)
                poster_path = f"images/{filename}"
            else:
                flash("Poster must be a PNG, JPG, JPEG, GIF, or SVG file.")
                return redirect(url_for("manage_movies"))

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute("""
            INSERT INTO movies (title, description, poster_path)
            VALUES (%s, %s, %s)
        """, (title, description, poster_path))

        movie_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO showtimes (movie_id, show_time, auditorium)
            VALUES (%s, %s, %s)
        """, (movie_id, show_time, auditorium))

        showtime_id = cursor.lastrowid

        create_seats_for_showtime(cursor, showtime_id)

        db.commit()
        db.close()

        flash("Movie, showtime, poster, and seats were added successfully.")
        return redirect(url_for("manage_movies"))

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT movies.id AS movie_id,
               movies.title,
               movies.description,
               movies.poster_path,
               showtimes.show_time,
               showtimes.auditorium
        FROM movies
        LEFT JOIN showtimes ON movies.id = showtimes.movie_id
        ORDER BY movies.id, showtimes.id
    """)

    movie_rows = cursor.fetchall()
    db.close()

    return render_template("manage_movies.html", movie_rows=movie_rows)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)