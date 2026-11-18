# Ask the customer to enter the total purchase amount
purchase_amount_str = input("Enter the total purchase amount (KSh): ")

# Convert the amount to a floating-point number
purchase_amount = float(purchase_amount_str)

# Use a comparison operator to determine whether the purchase amount is at least KSh 10,000
qualifies = purchase_amount >= 10000

# If the customer qualifies, calculate the discount (15% * Purchase Amount)
if qualifies:
    discount = 0.15 * purchase_amount
else:
    discount = 0.0

# Calculate the final amount (Purchase Amount - Discount)
final_amount = purchase_amount - discount

# Display the purchase amount, discount, and final amount
print("\n--- Supermarket Purchase Summary ---")
print(f"Purchase Amount: KSh {purchase_amount:.2f}")
print(f"Qualifies for Discount (>= 10,000): {qualifies}")
print(f"Discount: KSh {discount:.2f}")
print(f"Final Amount: KSh {final_amount:.2f}")