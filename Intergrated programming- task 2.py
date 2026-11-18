class Product:

  def __init__(self, name="", code="", price=0.0, quantity=0):
    self.name = name
    self.code = code
    self.price = price
    self.quantity = quantity

  def set_details(self, name, code, price, quantity):
    self.name = name
    self.code = code
    self.price = price
    self.quantity = quantity

  def calculate_stock_value(self):
    return self.price * self.quantity

  def display_info(self):
    stock_value = self.calculate_stock_value()
    print(
        f"Product: {self.name} | Code: {self.code} | Price: Kshs{self.price:.2f}"
        f" | Quantity: {self.quantity} | Stock Value: Kshs{stock_value:.2f}"
    )


# Main Execution
products = []
print("--- Enter Details for 3 Products ---")
for i in range(3):
  print(f"\nProduct {i+1}:")
  name = input("Enter Product Name: ")
  code = input("Enter Product Code: ")

  # Use try...except to handle invalid price input
  while True:
    try:
      price = float(input("Enter Price: "))
      if price >= 0:
        break
      print("Price cannot be negative.")
    except ValueError:
      print("Invalid input! Please enter a numeric value for price.")

  # Use try...except to handle invalid quantity input
  while True:
    try:
      quantity = int(input("Enter Quantity: "))
      if quantity >= 0:
        break
      print("Quantity cannot be negative.")
    except ValueError:
      print("Invalid input! Please enter an integer value for quantity.")

  p = Product()
  p.set_details(name, code, price, quantity)
  products.append(p)

print("\n--- Inventory Information ---")
total_inventory_value = 0
for product in products:
  product.display_info()
  total_inventory_value += product.calculate_stock_value()

# Calculate and display the total value of all products in stock
print(f"\nTotal Stock Value of All Products: kshs{total_inventory_value:.2f}")

# Save to inventory.txt and close file
file = open("inventory.txt", "w")
for product in products:
  stock_val = product.calculate_stock_value()
  file.write(
      f"Product: {product.name}, Code: {product.code}, Price:"
      f" {product.price}, Quantity: {product.quantity}, Stock Value:"
      f" {stock_val}\n"
  )
file.write(f"Total Inventory Value: {total_inventory_value}\n")
file.close()
print("\nInventory details successfully saved to 'inventory.txt'.")