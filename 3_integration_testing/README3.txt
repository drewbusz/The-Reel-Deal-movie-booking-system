Integration Testing

This folder contains integration testing documentation for The Reel Deal movie booking system. These tests confirm that the Flask web application, HTML templates, and MySQL database work together correctly.

The integration tests focus on full user workflows rather than individual functions. The main workflows tested were:

- Customer login and role-based navigation
- Movie and showtime display from the database
- Multi-seat selection and booking
- Automatic seat status updates after booking
- Booking confirmation and ticket code generation
- Staff ticket validation
- Staff booking dashboard display
- Staff movie and showtime creation
- Automatic seat map creation for newly added showtimes

Testing Method:
The integration testing was completed manually by running the Flask application locally, completing each workflow in the browser, and confirming that the expected database changes occurred in MySQL.

How to Run Integration Testing:
1. Open MySQL Workbench.
2. Run database.sql to reset and populate the reel_deal database.
3. Open the project folder in Visual Studio Code.
4. Confirm that DB_CONFIG in app.py matches the local MySQL login.
5. Start the Flask app by running:

python app.py

6. Open a browser and go to:

http://127.0.0.1:5000

7. Complete the test cases listed in integration_test_plan.txt.

Test Accounts:

Customer:
customer@test.com
password123

Staff:
staff@test.com
password123
