import mysql.connector

def show_seats(showtime_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database="reel_deal"
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT seat_label, status FROM seats WHERE showtime_id=%s ORDER BY seat_label",
        (showtime_id,)
    )

    seats = cursor.fetchall()

    print("\nSeat Availability:")
    for seat_label, status in seats:
        print(f"{seat_label} - {status}")

    db.close()


def reserve_seat(user_id, showtime_id, seat):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database="reel_deal"
    )

    cursor = db.cursor()

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
            "INSERT INTO bookings (user_id, showtime_id, seat_label) VALUES (%s, %s, %s)",
            (user_id, showtime_id, seat)
        )
        cursor.execute(
            "UPDATE seats SET status='reserved' WHERE seat_label=%s AND showtime_id=%s",
            (seat, showtime_id)
        )

        db.commit()
        print(f"Booking successful. Seat {seat} has been reserved.")
        db.close()
        return True
    else:
        print(f"Seat {seat} is already taken.")
        db.close()
        return False


if __name__ == "__main__":
    user_id = 1
    showtime_id = 1

    show_seats(showtime_id)

    seat = input("\nEnter the seat you want to reserve: ").strip().upper()

    reserve_seat(user_id, showtime_id, seat)
