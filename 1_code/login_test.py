import mysql.connector

def login(email, password):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password123",
        database="reel_deal"
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT role FROM users WHERE email=%s AND password=%s",
        (email, password)
    )

    user = cursor.fetchone()

    db.close()

    return user


if __name__ == "__main__":
    email = input("Enter email: ")
    password = input("Enter password: ")

    user = login(email, password)

    if user:
        print(f"Login successful. Role: {user[0]}")
    else:
        print("Invalid email or password.")
