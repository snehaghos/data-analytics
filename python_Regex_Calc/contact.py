import re
from decimal import Decimal
from collections import Counter

EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)

PHONE_PATTERN = re.compile(
    r"(?:\+91\s*)?[6-9]\d{4}\s*\d{5}"
)


def problem_01(text):
    return {
        "emails": EMAIL_PATTERN.findall(text),
        "phones": PHONE_PATTERN.findall(text),
    }


def test_01():
    result = problem_01(
        "Email: a@test.com Phone: +91 98765 43210"
    )

    assert result["emails"] == ["a@test.com"]
    assert result["phones"] == ["+91 98765 43210"]

    print("Test 01 passed!")


test_01()