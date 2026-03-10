import mysql.connector

def view_available_seats(showtime_id):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database="reel_deal"
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT seat_label, status FROM seats WHERE showtime_id=%s",
        (showtime_id,)
    )

    seats = cursor.fetchall()

    print("Seat availability:")
    for seat in seats:
        print(seat[0], "-", seat[1])

    db.close()

if __name__ == "__main__":
    view_available_seats(1)
