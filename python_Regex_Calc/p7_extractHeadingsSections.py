# 08. Extract Headings and Sections from PDF/Text Reports
# Level: Intermediate
# Real-Life Scenario
# A text-extracted report uses uppercase headings.
# You need to identify headings and capture the text belonging to each section
# until the next heading.
# Sample Input
# EXECUTIVE SUMMARY
# Revenue increased by 18 percent during the year.
# The company opened two new branches.
#
# FINANCIAL RESULTS
# Gross profit was ₹45,000,000.
# Operating expenses increased by 6 percent.
#
# RISK FACTORS
# Foreign exchange volatility remains a concern.
# Your Tasks
# 42. Identify each uppercase heading.
# 43. Capture the complete section body under each heading.
# 44. Stop the section at the next uppercase heading.
# 45. Preserve internal line breaks.
# 46. Return a list of dictionaries with heading and body.
# 47. Do not assume that every uppercase word inside a paragraph is a heading.

import sys
import re

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')


HEADING_SECTION_PATTERN = re.compile(
    r"(?P<heading>^[A-Z][A-Z\s]{2,}$)\s*(?P<body>.+?)(?=^[A-Z][A-Z\s]{2,}$|\Z)",
    re.MULTILINE | re.DOTALL,
)


def problem_07(text):
    """Extract headings and their section bodies from a report."""
    raw_matches = list(HEADING_SECTION_PATTERN.finditer(text))
    print("Raw matches:")
    for m in raw_matches:
        print(f"  Heading: {m.group('heading')!r}")
        print(f"  Body preview: {m.group('body')[:60]!r}...")

    sections = []
    for m in raw_matches:
        body = m.group("body").strip()
        sections.append({
            "heading": m.group("heading").strip(),
            "body": body,
        })

    return sections


# --- Test Cases ---

sample = """EXECUTIVE SUMMARY
Revenue increased by 18 percent during the year.
The company opened two new branches.

FINANCIAL RESULTS
Gross profit was ₹45,000,000.
Operating expenses increased by 6 percent.

RISK FACTORS
Foreign exchange volatility remains a concern."""

print("Test Case 1: Sample report")
for s in problem_07(sample):
    print(f"  [{s['heading']}]")
    print(f"  {s['body']}\n")

test2 = """INTRODUCTION
This document covers the quarterly review.

SECTION A
First section content here.

SECTION B
Second section content.
Multiple lines in this body.

CONCLUSION
Final remarks."""
print("Test Case 2: Four sections")
for s in problem_07(test2):
    print(f"  [{s['heading']}] {s['body'][:40]}...\n")

test3 = """SINGLE HEADING
Just one section and nothing else."""
print("Test Case 3: Single heading")
print(problem_07(test3))

test4 = """No headings here. Just lowercase text with SOME uppercase words
scattered like ERROR or WARNING but they are not headings."""
print("\nTest Case 4: No real headings")
print(problem_07(test4))

test5 = """ALPHA
Body one.

BETA
Body two.

GAMMA
Body three.
With extra line.

DELTA
Final section."""
print("\nTest Case 5: Four short sections")
for s in problem_07(test5):
    print(f"  [{s['heading']}] {s['body'][:30]}...\n")
