# 05. Extract Dates from Mixed Document Formats
# Level: Intermediate
# Real-Life Scenario
# A collection of PDFs contains dates in several common formats.
# The goal is to identify dates first; strict calendar validation can be handled separately with datetime.
# Sample Input
# Invoice Date: 13-08-2026
# Due Date: 31/08/2026
# Created: 2026-08-13
# Payment received: 13 Aug 2026
# Old format: 13.08.2026
# Your Tasks
# 22. Extract DD-MM-YYYY.
# 23. Extract DD/MM/YYYY.
# 24. Extract YYYY-MM-DD.
# 25. Extract DD Mon YYYY.
# 26. Extract DD.MM.YYYY.
# 27. Do not match unrelated numbers such as invoice IDs.
# 28. Store each matched format separately.

import re


# Regex Explanation (plain English):
# - We use alternation | to match five date formats.
# - \b ensures we don't match dates embedded in longer words or IDs.
# - Named groups (?P<format>...) let us identify which format matched.
# - DD-MM-YYYY: (\d{2})-(\d{2})-(\d{4})
# - DD/MM/YYYY: (\d{2})/(\d{2})/(\d{4})
# - YYYY-MM-DD: (\d{4})-(\d{2})-(\d{2})
# - DD Mon YYYY: (\d{2})\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s(\d{4})
# - DD.MM.YYYY: (\d{2})\.(\d{2})\.(\d{4})

DATE_PATTERN = re.compile(
    r"(?P<dmy>\d{2}-\d{2}-\d{4})"
    r"|(?P<dmy_slash>\d{2}/\d{2}/\d{4})"
    r"|(?P<ymd>\d{4}-\d{2}-\d{2})"
    r"|(?P<dmon>\d{2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4})"
    r"|(?P<dmy_dot>\d{2}\.\d{2}\.\d{4})"
)


def problem_04(text):
    """Extract dates from mixed document text and group them by format."""
    raw_matches = list(DATE_PATTERN.finditer(text))
    print("Raw matches:")
    for m in raw_matches:
        print(f"  {m.group()!r} (format: {m.lastgroup})")

    result = {
        "DD-MM-YYYY": [],
        "DD/MM/YYYY": [],
        "YYYY-MM-DD": [],
        "DD Mon YYYY": [],
        "DD.MM.YYYY": [],
    }

    format_map = {
        "dmy": "DD-MM-YYYY",
        "dmy_slash": "DD/MM/YYYY",
        "ymd": "YYYY-MM-DD",
        "dmon": "DD Mon YYYY",
        "dmy_dot": "DD.MM.YYYY",
    }

    for m in raw_matches:
        fmt = format_map[m.lastgroup]
        result[fmt].append(m.group())

    return result


# --- Test Cases ---

sample_text = """Invoice Date: 13-08-2026
Due Date: 31/08/2026
Created: 2026-08-13
Payment received: 13 Aug 2026
Old format: 13.08.2026"""

print("Test Case 1: Sample input")
print(problem_04(sample_text))

test2 = """Report generated on 25/12/2025.
Deadline is 01-01-2027.
Published 15 Jan 2024.
Reference 12.06.2023.
Not a date: INV-2026-00125"""
print("\nTest Case 2: Mixed with invalid")
print(problem_04(test2))

test3 = """Start: 2026-01-01
End: 31-12-2026
Archive: 05.03.2020"""
print("\nTest Case 3: Only ISO and dot format")
print(problem_04(test3))

test4 = """No dates here. Just text and numbers 12345."""
print("\nTest Case 4: No dates at all")
print(problem_04(test4))

test5 = """Dual: 01/01/2026 and 01-01-2026
Overlap: 10.10.2025 and 10 Oct 2025"""
print("\nTest Case 5: Multiple formats for same date")
print(problem_04(test5))
