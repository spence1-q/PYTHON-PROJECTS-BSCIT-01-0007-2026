# Ask the customer to enter details
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
quantity_input = input("Enter quantity purchased: ")
price_input = input("Enter price per item: ")

#  Convert quantity to an integer and price to a float
quantity = int(quantity_input)
price = float(price_input)

# Calculate the total cost
# Calculate total cost by multiplying the quantity purchased by the price per item
total_cost = quantity * price

# Display information using an f-string, with price and total cost to three decimal places
print("\n--- Purchase Receipt ---")
print(f"Customer Name: {customer_name}")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Price per Item: {price:.3f}")
print(f"Total Cost: {total_cost:.3f}")