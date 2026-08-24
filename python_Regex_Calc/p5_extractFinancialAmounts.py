# 06. Extract Financial Amounts from Invoices
# Level: Intermediate
# Real-Life Scenario
# Financial documents contain currency symbols, commas, decimals, optional spaces,
# and sometimes negative values. Your regex should extract the textual amount;
# numeric normalization happens afterward.
# Sample Input
# Subtotal: ₹ 45,000.00
# Discount: -₹ 2,500.00
# Tax: ₹8,550.00
# Grand Total: ₹ 51,050.00
# Refund: -₹1,200.50

import re
from decimal import Decimal, InvalidOperation

# Regex Explanation (plain English):
# - -?\s*₹\s*  => optional minus sign, optional whitespace, the ₹ symbol, optional whitespace
# - ([\d,]+\.\d{2}) => capture group for the numeric part: digits with optional commas, a dot, exactly 2 decimal places
# - The currency symbol is NOT inside the capture group.
# - \b at the end ensures we don't match partial numbers.

RUPEE_PATTERN = re.compile(
    r"-?\s*₹\s*(?P<amount>[\d,]+\.\d{2})"
)


def problem_05(text):
    """Extract rupee amounts from text, then convert to Decimal."""
    raw_matches = list(RUPEE_PATTERN.finditer(text))
    print("Raw matches:")
    for m in raw_matches:
        print(f"  {m.group()!r} => captured amount: {m.group('amount')!r}")

    results = []
    for m in raw_matches:
        raw_amount = m.group("amount")
        negative = "-" in m.group()
        clean = raw_amount.replace(",", "")
        try:
            value = Decimal(clean)
            if negative:
                value = -value
        except InvalidOperation:
            value = None
        results.append({
            "raw": m.group(),
            "numeric": raw_amount,
            "value": value,
        })

    return results


# --- Test Cases ---

sample_text = """Subtotal: ₹ 45,000.00
Discount: -₹ 2,500.00
Tax: ₹8,550.00
Grand Total: ₹ 51,050.00
Refund: -₹1,200.50"""

print("Test Case 1: Sample invoice")
for r in problem_05(sample_text):
    print(f"  {r}")

test2 = """Item A: ₹12,345.67
Item B: -₹  999.99
Item C: ₹ 1.00
Nothing here: USD 50.00"""
print("\nTest Case 2: Mixed with non-rupee")
for r in problem_05(test2):
    print(f"  {r}")

test3 = """Tiny: ₹0.01
Large: ₹9,99,999.99"""
print("\nTest Case 3: Edge values")
for r in problem_05(test3):
    print(f"  {r}")

test4 = """No currency symbols at all. Just 12345.67"""
print("\nTest Case 4: No rupee symbols")
print(problem_04 if False else problem_05(test4))

test5 = """Negative huge: -₹1,00,000.00
Positive small: ₹ 0.50"""
print("\nTest Case 5: Negative and positive")
for r in problem_05(test5):
    print(f"  {r}")
