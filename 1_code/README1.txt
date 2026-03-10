This folder contains the source code for the Reel Deal movie booking system prototype.

At the time of the midterm submission, several Python test scripts demonstrate core system functionality using a MySQL database. These scripts implement basic versions of key system behaviors:

- login_test.py: prompts the user for an email and password, then demonstrates user authentication by checking the entered credentials against the users table and returning the user role if login is successful.

- view_seats_test.py: retrieves and displays seat availability for a selected showtime.

- booking_test.py: displays seat availability for a showtime, prompts the user to enter a seat label, checks whether the selected seat is available, creates a booking record, and updates the seat status to help prevent double booking.

The database_schema.sql file defines the basic database structure used by these scripts, including the users, seats, and bookings tables, along with sample test data for demonstration.

To run the prototype, MySQL Server must be installed and running, the reel_deal database must be created, and the schema in database_schema.sql must be executed before running the Python scripts. The scripts also require the mysql-connector-python package.

Future development will include implementing movie and showtime selection, manager functions for maintaining movies and showtimes, expanded booking management features, ticket validation, and a more complete user-facing interface.

I would also add a short How to Run section underneath it if you do not already have one, because the assignment specifically wants instructions.
