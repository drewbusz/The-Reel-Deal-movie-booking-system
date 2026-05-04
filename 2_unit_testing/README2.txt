Unit Testing

This folder contains unit tests for individual functions used in The Reel Deal movie booking system. These tests focus on smaller pieces of application logic rather than the full customer or staff workflow.

The unit tests cover:

- Ticket code generation
- Poster file extension validation
- Automatic seat label generation logic

These tests help confirm that important helper functions behave correctly before they are used in the full Flask application.

Required Software:
- Python 3
- pytest

To install pytest, run:

python -m pip install pytest

To run the unit tests, open a terminal in this folder and run:

python -m pytest

Test Files:

test_ticket_code.py
Checks that generated ticket codes use the expected format and length.

test_allowed_file.py
Checks that accepted poster file types are allowed and unsupported file types are rejected.

test_seat_generation.py
Checks that the expected seating layout includes rows A-D and seats 1-8, for a total of 32 seats.
