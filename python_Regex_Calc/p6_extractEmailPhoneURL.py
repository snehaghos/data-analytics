# 07. Extract Email, Phone and URL Data from Web Page Text
# Level: Intermediate
# Real-Life Scenario
# You scrape a web page and first convert its visible content to text.
# The page contains navigation text, contact details, social links, and unrelated numbers.
# Sample Input
# Contact us at sales@example.com or support@example.org.
# Call +91 98765 43210 for sales.
# Documentation: https://docs.example.com/python/regex
# Company site: https://www.example.com
# Copyright 2026.
# Your Tasks
# 36. Extract email addresses.
# 37. Extract Indian phone numbers with optional +91 and optional spaces.
# 38. Extract HTTP/HTTPS URLs.
# 39. Do not treat the year 2026 as a phone number.
# 40. Remove trailing punctuation from URLs if present.
# 41. Return a dictionary containing emails, phones, and URLs.

import sys
import re


if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')


EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_PATTERN = re.compile(r"(?:\+91\s*)?[6-9]\d{4}\s*\d{5}")
URL_PATTERN = re.compile(r"https?://[^\s<>\"]+")


def problem_06(text):
    """Extract emails, phones, and URLs from web page text."""
    raw_emails = EMAIL_PATTERN.findall(text)
    raw_phones = PHONE_PATTERN.findall(text)
    raw_urls = URL_PATTERN.findall(text)


    clean_urls = [re.sub(r"[.,;:!?)]+$", "", u) for u in raw_urls]

    print("Raw emails:", raw_emails)
    print("Raw phones:", raw_phones)
    print("Raw URLs:", raw_urls)
    print("Cleaned URLs:", clean_urls)

    return {
        "emails": raw_emails,
        "phones": raw_phones,
        "urls": clean_urls,
    }


# --- Test Cases ---

sample = """Contact us at sales@example.com or support@example.org.
Call +91 98765 43210 for sales.
Documentation: https://docs.example.com/python/regex
Company site: https://www.example.com
Copyright 2026."""

print("Test Case 1: Sample input")
print(problem_06(sample))

test2 = """Reach hr@company.in or admin@test.co.in.
Mobile: 9123456789 and +91 76543 21098.
Visit http://blog.example.org and https://shop.example.com/?q=test."""
print("\nTest Case 2: Multiple contacts and URLs")
print(problem_06(test2))

test3 = """Not a phone: 2026.
Not an email: @missing.com
Broken URL: https://"""
print("\nTest Case 3: Invalid inputs")
print(problem_06(test3))

test4 = """Email: john.doe+tag@sub.domain.co.uk
Phone: 88888 12345
URL: https://example.com/path/to/page.html"""
print("\nTest Case 4: Complex valid inputs")
print(problem_06(test4))

test5 = """No contacts, just random text about 100 items and 50% discount."""
print("\nTest Case 5: No matches")
print(problem_06(test5))
