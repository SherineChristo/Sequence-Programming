"""
Program: Farmer Problem (Menu Driven with User Input)

This program solves different farmer-related problems
based on the user's choice.
"""

print("------ Farmer Problem Menu ------")
print("1. Farmer Profit or Loss")
print("2. Farmer Land Area Calculation")
print("3. Farmer Crop Income Calculation")
print("4. Farmer River Crossing Logic")

choice = int(input("Enter your choice (1-4): "))

# --------------------------------------------------
# 1. FARMER PROFIT OR LOSS
# --------------------------------------------------
if choice == 1:
    cost_price = float(input("Enter Cost Price: "))
    selling_price = float(input("Enter Selling Price: "))

    if selling_price > cost_price:
        profit = selling_price - cost_price
        print("Profit:", profit)
    else:
        loss = cost_price - selling_price
        print("Loss:", loss)

# --------------------------------------------------
# 2. FARMER LAND AREA CALCULATION
# --------------------------------------------------
elif choice == 2:
    length = float(input("Enter length of land (meters): "))
    breadth = float(input("Enter breadth of land (meters): "))

    area = length * breadth
    print("Area of land:", area, "sq.m")

# --------------------------------------------------
# 3. FARMER CROP INCOME CALCULATION
# --------------------------------------------------
elif choice == 3:
    acres = float(input("Enter number of acres: "))
    income_per_acre = float(input("Enter income per acre: "))

    total_income = acres * income_per_acre
    print("Total Crop Income:", total_income)

# --------------------------------------------------
# 4. FARMER RIVER CROSSING (LOGIC ONLY)
# --------------------------------------------------
elif choice == 4:
    print("Farmer must take one item at a time.")
    print("Goat cannot be left with cabbage or wolf.")
    print("Follow logical steps to cross the river.")

# --------------------------------------------------
# INVALID CHOICE
# --------------------------------------------------
else:
    print("Invalid choice! Please select between 1 and 4.")

# --------------------------------------------------
# END OF PROGRAM
# --------------------------------------------------
