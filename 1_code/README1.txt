The Reel Deal - Final Source Code

This folder contains the final source code for The Reel Deal, a movie ticket booking system built with Python Flask, MySQL, HTML, and CSS.

The final application includes both customer and staff functionality. Customers can log in, browse available movies and showtimes, view movie posters, select one or more seats from a visual seat map, and receive a ticket code after booking. Staff users can validate ticket codes, view booking records, and manage movies by adding new movie titles, descriptions, showtimes, auditorium numbers, and poster images.

The system automatically handles several important tasks. When a customer books tickets, the application checks seat availability, prevents already reserved seats from being selected, creates booking records, generates a ticket code, and updates the selected seats to reserved in the database. When staff add a new showtime, the system automatically creates a full seat map with rows A-D and seats 1-8 for that showtime.

Required Software:
- Python 3
- MySQL Server
- MySQL Workbench
- Visual Studio Code or another code editor

Required Python Packages:
- flask
- mysql-connector-python
- werkzeug

To install the required packages, run:

python -m pip install flask mysql-connector-python werkzeug

Project Files:
- app.py: main Flask application file
- database.sql: creates and populates the MySQL database
- templates/: contains the HTML templates used by the Flask app
- static/images/: contains movie poster images and uploaded poster files

How to Set Up the Database:
1. Open MySQL Workbench.
2. Connect to the local MySQL Server instance.
3. Open database.sql.
4. Run the full script.
5. Confirm that the reel_deal database was created.

The database.sql script creates the following tables:
- users
- movies
- showtimes
- seats
- bookings

The script also inserts sample users, movies, showtimes, posters, and seat data.

How to Run the Application:
1. Open the project folder in Visual Studio Code.
2. Confirm that app.py has the correct MySQL username and password in the DB_CONFIG section.
3. Open a terminal in the project folder.
4. Run:

python app.py

5. Open a browser and go to:

http://127.0.0.1:5000

Test Login Credentials:

Customer Account:
Email: customer@test.com
Password: password123

Staff Account:
Email: staff@test.com
Password: password123

Customer Features:
- Log in as a customer
- Browse movies and showtimes
- View movie posters
- Select one or more seats
- See selected seats turn gray before booking
- Submit a booking
- Receive a ticket confirmation code

Staff Features:
- Log in as a staff user
- Validate customer ticket codes
- Mark active tickets as used
- View the staff booking dashboard
- Add new movies
- Add movie descriptions
- Add showtimes
- Add auditorium numbers
- Upload movie poster images
- Automatically create seats for newly added showtimes

Notes:
This project is intended as a local demonstration system for a course project. It uses plain text test passwords for simplicity in the demo environment. In a production system, passwords should be hashed, database credentials should be stored securely, and additional input validation and security controls should be added.
