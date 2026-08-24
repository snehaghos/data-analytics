import re


def problem_02(text):

    cleaned_text=re.sub(r"\s+"," ",text).strip()

    invoice_match = re.search(
        r"\bInvoice No:\s*([A-Z0-9-]+)",
        cleaned_text
    )

    customer_match = re.search(
        r"\bCustomer:\s*(.*?)\s*Address:",
        cleaned_text
    )

    amount_match = re.search(
        r"₹\s*([\d,]+\.\d{2})",
        cleaned_text
    )

    print("Raw invoice match:", invoice_match.group(0) if invoice_match else None)
    print("Raw customer match:", customer_match.group(0) if customer_match else None)
    print("Raw amount match:", amount_match.group(0) if amount_match else None)

    return {
        "cleaned_text": cleaned_text,
        "invoice_no": invoice_match.group(1) if invoice_match else None,
        "customer": customer_match.group(1) if customer_match else None,
        "amount": amount_match.group(1) if amount_match else None,
    }



text1 = """Invoice No:     INV-2026-00125
Customer:    ABC Hardware Pvt. Ltd.
Address:  15   Park Street,   Kolkata
Total:     ₹ 12,450.00
Status:     PAID"""

result = problem_02(text1)

print("\nResult:")
print(result)



text2 = """Invoice No:        INV-2026-00999

Customer:     XYZ Traders Ltd.

Address:     20     MG Road,      Kolkata

Total:       ₹ 98,750.50

Status: PAID"""

print("\n--- Test Case 2 ---")
print(problem_02(text2))



text3 = (
    "Invoice No:\tINV-2026-00045\n"
    "Customer:\t\tModern Tools Pvt. Ltd.\n"
    "Address:\t10\tPark Street, Kolkata\n"
    "Total:\t₹ 5,500.00\n"
    "Status:\tPAID"
)

print("\n--- Test Case 3 ---")
print(problem_02(text3))


text4 = """Customer: Unknown Company
Address: Kolkata
Status: PAID"""

print("\n--- Test Case 4: Invalid Input ---")
print(problem_02(text4))