import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "1_code")))

from app import allowed_file


def test_allowed_poster_files():
    assert allowed_file("poster.png") is True
    assert allowed_file("poster.jpg") is True
    assert allowed_file("poster.jpeg") is True
    assert allowed_file("poster.gif") is True
    assert allowed_file("poster.svg") is True


def test_disallowed_poster_files():
    assert allowed_file("poster.exe") is False
    assert allowed_file("poster.pdf") is False
    assert allowed_file("poster.txt") is False
    assert allowed_file("poster") is False