Data Collection

This folder contains data collection and database setup information for The Reel Deal movie booking system.

The project does not use live external data collection. Instead, it uses manually created sample data to demonstrate the system's main features. The sample data includes users, movies, showtimes, auditorium information, poster paths, seat records, and booking records created during testing.

The database.sql file creates the reel_deal database and inserts the starting sample data used for the final project demo.

Data Included:
- Customer and staff test users
- Sample movies
- Movie descriptions
- Movie poster file paths
- Showtime records
- Auditorium numbers
- Seat records for each showtime
- Booking records created during application testing

Seat Data:
Each showtime uses an automatically generated seating layout with four rows and eight seats per row:

A1-A8
B1-B8
C1-C8
D1-D8

This creates 32 seats for each showtime.

How to Recreate the Data:
1. Open MySQL Workbench.
2. Connect to the local MySQL Server instance.
3. Open database.sql.
4. Run the full script.
5. Confirm that the reel_deal database was created.

Verification Queries:
After running database.sql, the following queries can be used to confirm that the sample data was created correctly:

USE reel_deal;

SELECT * FROM users;
SELECT * FROM movies;
SELECT * FROM showtimes;
SELECT COUNT(*) AS total_seats FROM seats;

Expected Results:
- users table should include a customer and staff account
- movies table should include the sample movies
- showtimes table should include sample showtimes
- seats table should include automatically generated seats for each showtime

Purpose of Sample Data:
The sample data allows the final demo to show the full customer and staff workflow without requiring outside data sources. It supports movie browsing, showtime selection, seat reservation, booking confirmation, ticket validation, and staff movie management.
