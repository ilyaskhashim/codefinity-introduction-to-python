# Input variables
product_type = "Dairy"
day_of_week   = "Wednesday"

# 1) Fruits + Monday
if product_type == "Fruits" and day_of_week == "Monday":
    print("10% discount on Fruits today!")

# 2) Vegetables + Tuesday
elif product_type == "Vegetables" and day_of_week == "Tuesday":
    print("15% discount on Vegetables today!")

# 3) Dairy + Wednesday
elif product_type == "Dairy" and day_of_week == "Wednesday":
    print("20% discount on Dairy today!")

# 4) Other product type
elif product_type == "Other":
    print("No discount available.")

# 5) Everything else
else:
    print("No special discounts today.")