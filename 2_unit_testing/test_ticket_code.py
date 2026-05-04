import re
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "1_code")))

from app import generate_ticket_code


def test_ticket_code_format():
    ticket_code = generate_ticket_code()

    assert ticket_code.startswith("TCK-")
    assert len(ticket_code) == 10
    assert re.match(r"^TCK-[A-Z0-9]{6}$", ticket_code)