# #03. Extract Invoice Line Items from Semi-Structured Text
# Level: Beginner → Intermediate
# Real-Life Scenario
# A PDF invoice has been converted to text. Each item is approximately represented as SKU, description, quantity, unit price, and amount, but spacing is inconsistent.
# Sample Input
# SKU       Description                 Qty    Rate       Amount
# KB-1001   Keyboard Mechanical          2      2,499.00   4,998.00
# MS-2205   Wireless Mouse               3      899.00     2,697.00
# USB-10    USB-C Cable                  5      299.00     1,495.00
# Your Tasks
# 11.	Extract each line item separately.
# 12.	Capture SKU, description, quantity, rate, and amount.
# 13.	Use named groups for the five fields.
# 14.	Allow variable whitespace between columns.
# 15.	Do not accidentally parse the header as an item.
# 16.	Convert the extracted quantity to int and monetary values to numbers after regex extraction.
# Concepts to Practice
# named groups, whitespace matching, line anchors, re.MULTILINE, finditer()
# Guidance / Hint
# The SKU is a strong anchor. Use a line-based pattern rather than a single pattern over the entire document.
# Self-Work Requirements
# •	Write at least 3 additional test cases.
# •	Include at least one invalid or unexpected input.
# •	Print or inspect the raw matches before converting them into final values.
# •	Explain your regex in plain English.
# •	If the pattern is becoming very long, consider splitting the problem into multiple smaller patterns.
#  


import re


def problem_03(text):
	"""Extract invoice rows, then convert quantity and monetary fields."""
	line_item_pattern = re.compile(
		r"^[ \t]*(?P<sku>[A-Z0-9]+(?:-[A-Z0-9]+)+)[ \t]+"
		r"(?P<description>.+?)[ \t]+"
		r"(?P<quantity>\d+)[ \t]+"
		r"(?P<rate>[\d,]+\.\d{2})[ \t]+"
		r"(?P<amount>[\d,]+\.\d{2})[ \t]*$",
		re.MULTILINE,
	)

	raw_matches = list(line_item_pattern.finditer(text))
	print("Raw matches:")
	for match in raw_matches:
		print(match.groupdict())

	items = []
	for match in raw_matches:
		fields = match.groupdict()
		items.append(
			{
				"sku": fields["sku"],
				"description": fields["description"].strip(),
				"quantity": int(fields["quantity"]),
				"rate": float(fields["rate"].replace(",", "")),
				"amount": float(fields["amount"].replace(",", "")),
			}
		)

	return items



sample_text = """SKU       Description                 Qty    Rate       Amount
KB-1001   Keyboard Mechanical          2      2,499.00   4,998.00
MS-2205   Wireless Mouse               3      899.00     2,697.00
USB-10    USB-C Cable                  5      299.00     1,495.00"""

print("Test Case 1: Sample invoice")
print(problem_03(sample_text))


test_case_2 = "SKU\tDescription\tQty\tRate\tAmount\nAA-1\tDesk Lamp\t1\t1,250.00\t1,250.00"
print("\nTest Case 2: Tabs")
print(problem_03(test_case_2))


test_case_3 = "CC-9    USB-C Cable (1m)    2    299.00    598.00"
print("\nTest Case 3: Punctuation in description")
print(problem_03(test_case_3))


test_case_4 = """SKU Description Qty Rate Amount
INVALID ROW WITHOUT NUMBERS
GOOD-7   Notebook, A5   4   75.00   300.00"""
print("\nTest Case 4: Invalid row is ignored")
print(problem_03(test_case_4))


