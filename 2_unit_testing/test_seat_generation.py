def generate_expected_seat_labels():
    rows = ["A", "B", "C", "D"]
    numbers = range(1, 9)

    seats = []

    for row in rows:
        for number in numbers:
            seats.append(f"{row}{number}")

    return seats


def test_seat_layout_has_32_seats():
    seats = generate_expected_seat_labels()

    assert len(seats) == 32


def test_seat_layout_starts_with_a1_and_ends_with_d8():
    seats = generate_expected_seat_labels()

    assert seats[0] == "A1"
    assert seats[-1] == "D8"


def test_seat_layout_contains_expected_rows():
    seats = generate_expected_seat_labels()

    assert "A1" in seats
    assert "B8" in seats
    assert "C4" in seats
    assert "D8" in seats