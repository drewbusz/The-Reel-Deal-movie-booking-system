import mysql.connector

def reserve_seat(user_id, showtime_id, seat):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database="reel_deal"
    )

    cursor = db.cursor()

    # Check if the seat exists and is available
    cursor.execute(
        "SELECT status FROM seats WHERE seat_label=%s AND showtime_id=%s",
        (seat, showtime_id)
    )
    result = cursor.fetchone()

    if not result:
        print("Seat not found.")
        db.close()
        return False

    if result[0] == "available":
        cursor.execute(
            "INSERT INTO bookings (user_id, showtime_id, seat_label) VALUES (%s,%s,%s)",
            (user_id, showtime_id, seat)
        )
        cursor.execute(
            "UPDATE seats SET status='reserved' WHERE seat_label=%s AND showtime_id=%s",
            (seat, showtime_id)
        )

        db.commit()
        print("Booking successful. Seat reserved.")
        db.close()
        return True

    else:
        print("Seat is already taken.")
        db.close()
        return False


if __name__ == "__main__":
    reserve_seat(1, 1, "A3")