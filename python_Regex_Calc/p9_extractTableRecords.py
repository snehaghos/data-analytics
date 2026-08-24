# 10. Extract Table-Like Records from HTML/Text
# Level: Intermediate
# Real-Life Scenario
# A web table has been copied as text after HTML extraction.
# The columns are separated by variable whitespace and prices may contain commas.
# Sample Input
# Product       Category       Price       Stock
# Laptop Pro    Electronics    ₹75,999.00   12
# Office Chair  Furniture      ₹8,499.00    35
# Monitor 24    Electronics    ₹14,999.00   8
# Your Tasks
# 54. Skip the header.
# 55. Extract product, category, price, and stock.
# 56. Support spaces inside the product name.
# 57. Capture the price as text and normalize it afterward.
# 58. Return structured records.
# 59. Explain why a naive '\\S+' pattern cannot capture the product name correctly.

import sys
import re
from decimal import Decimal


if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')


TABLE_ROW_PATTERN = re.compile(
    r"^[ \t]*(?P<product>[\w][\w ]*[\w])\s+"
    r"(?P<category>[A-Za-z]+)\s+"
    r"(?P<price>₹[\d,]+\.\d{2})\s+"
    r"(?P<stock>\d+)\s*$",
    re.MULTILINE,
)


def problem_09(text):
    """Extract table records from text, normalize price to Decimal."""
    raw_matches = list(TABLE_ROW_PATTERN.finditer(text))
    print("Raw matches:")
    for m in raw_matches:
        print(f"  {m.groupdict()}")

    records = []
    for m in raw_matches:
        d = m.groupdict()
        price_str = d["price"].replace("₹", "").replace(",", "")
        records.append({
            "product": d["product"],
            "category": d["category"],
            "price": Decimal(price_str),
            "stock": int(d["stock"]),
        })

    return records


# --- Test Cases ---

sample = """Product       Category       Price       Stock
Laptop Pro    Electronics    ₹75,999.00   12
Office Chair  Furniture      ₹8,499.00    35
Monitor 24    Electronics    ₹14,999.00   8"""

print("Test Case 1: Sample table")
for r in problem_09(sample):
    print(f"  {r}")

test2 = """Product Category Price Stock
Wireless Keyboard  Electronics  ₹2,499.00  50
Standing Desk  Furniture  ₹15,000.00  10
USB Hub 3.0  Electronics  ₹899.00  200"""

print("\nTest Case 2: Different products")
for r in problem_09(test2):
    print(f"  {r}")

test3 = """Product     Category    Price      Stock
Gaming Mouse XL  Electronics  ₹4,999.00  25
Ergonomic Chair Pro  Furniture  ₹25,000.00  5"""

print("\nTest Case 3: Multi-word product names")
for r in problem_09(test3):
    print(f"  {r}")

test4 = """Just some random text without table format
Product Category Price Stock
No data rows here."""

print("\nTest Case 4: No data rows (header only)")
print(problem_09(test4))

test5 = """Product  Category  Price  Stock
Laptop  Electronics  ₹999.99  1
Single Item  Furniture  ₹1,00,000.00  0"""

print("\nTest Case 5: Edge values (999.99, zero stock)")
for r in problem_09(test5):
    print(f"  {r}")
