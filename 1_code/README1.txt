This folder contains the source code for The Reel Deal movie booking system prototype.

At the time of the midterm submission, several Python test scripts demonstrate core system functionality using a MySQL database. These scripts implement basic versions of key system behaviors:

- login_test.py: demonstrates user authentication by checking login credentials against the users table.
- view_seats_test.py: retrieves and displays seat availability for a selected showtime.
- booking_test.py: checks whether a seat is available, creates a booking record, and updates the seat status to prevent double booking.

The database_schema.sql file defines the basic database structure used by these scripts, including the users, seats, and bookings tables, along with sample test data for demonstration.

Future development will include implementing the movie selection interface, expanded seat reservation features, booking management, ticket validation, and a complete user interface for interacting with the system.
