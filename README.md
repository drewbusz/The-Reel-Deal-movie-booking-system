# The Reel Deal Movie Booking System

Drew Busz  
Final Project  

## Overview

The Reel Deal is a Flask and MySQL movie ticket booking system. The final version supports both customer and staff workflows. Customers can browse movies, view posters, select showtimes, choose one or more seats from a visual seat map, and receive a ticket code after booking. Staff users can validate tickets, view booking records, and manage movies, showtimes, auditorium information, and poster images.

## Demo Video

Final demo video:  
https://drive.google.com/file/d/1g5zMUDdWT8cNxn073E3hcontzE7mqAM4/view?usp=sharing

## Project Webpage

GitHub Repository:  
https://github.com/drewbusz/The-Reel-Deal-movie-booking-system

## What Is Included

- `1_code`: Final Flask application source code, templates, static files, database script, and README1.txt
- `2_unit_testing`: Unit test files and README2.txt
- `3_integration_testing`: Integration test plan, screenshots, and README3.txt
- `4_data_collection`: Database setup, sample data description, and README4.txt
- `5_documentation`: Final system requirements documentation, brochure, and presentation slides

## Final System Features

- Customer and staff login
- Role-based navigation
- Movie poster display
- Movie and showtime browsing
- Visual seat map with rows A-D and seats 1-8
- Multiple seats per booking
- Automatic ticket code generation
- Database-backed booking records
- Automatic seat status updates to prevent double booking
- Staff ticket validation
- Used-ticket prevention
- Staff booking dashboard
- Staff movie and showtime management
- Staff poster upload
- Automatic seat creation for newly added showtimes

## Technologies Used

- Python 3
- Flask
- MySQL Server
- MySQL Connector for Python
- HTML
- CSS
- Werkzeug file upload utilities

## How to Run the Project

1. Install Python 3.
2. Install MySQL Server and MySQL Workbench.
3. Install the required Python packages:

   python -m pip install flask mysql-connector-python werkzeug

4. Open MySQL Workbench and run the `database.sql` file from the `1_code` folder.
5. Open the project in Visual Studio Code or another editor.
6. In `app.py`, confirm that the MySQL username and password in `DB_CONFIG` match your local MySQL setup.
7. Run the application:

   python app.py

8. Open a browser and go to:

   http://127.0.0.1:5000

## Test Login Credentials

Customer account:

Email: customer@test.com  
Password: password123

Staff account:

Email: staff@test.com  
Password: password123

## Final Notes

This project is designed as a local course demonstration system. It uses sample movie data, test login accounts, and a local MySQL database. In a production version, passwords should be hashed, database credentials should be stored securely, and additional validation and security controls should be added.
