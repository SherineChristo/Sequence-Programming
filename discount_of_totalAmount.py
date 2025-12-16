"""
Program: Discount Calculation on Total Amount

This program calculates the discount amount
and the final payable amount.
"""

# --------------------------------------------------
# INPUT VALUES
# --------------------------------------------------

total_amount = 5000     # Total bill amount
discount_percent = 10   # Discount percentage

# --------------------------------------------------
# CALCULATION
# --------------------------------------------------

discount_amount = (total_amount * discount_percent) / 100
final_amount = total_amount - discount_amount

# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

print("Total Amount:", total_amount)                 # Output: 5000
print("Discount Percentage:", discount_percent)      # Output: 10
print("Discount Amount:", discount_amount)            # Output: 500.0
print("Final Payable Amount:", final_amount)          # Output: 4500.0

# --------------------------------------------------
# END OF PROGRAM
# --------------------------------------------------
