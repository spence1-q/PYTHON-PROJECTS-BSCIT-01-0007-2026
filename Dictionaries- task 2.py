# Create a dictionary named inventory containing at least five products and their quantities
inventory = {
    "Mandazi": 50,
    "Bread": 30,
    "Eggs": 120,
    "Sugar": 45,
    "Rice": 60
}

print("--- Initial Inventory ---")
print(inventory)

# Display the quantity of a specified product (e.g., "Mandazi")
product_to_check = "Mandazi"
print(f"\n--- Quantity of '{product_to_check}' ---")
print(f"{product_to_check}: {inventory[product_to_check]} units")

# Add a new product to the dictionary
new_product = "Butter"
new_quantity = 25
inventory[new_product] = new_quantity
print(f"\n--- Added New Product ({new_product}) ---")
print(f"Added {new_product} with quantity {new_quantity}")

# Update the quantity of an existing product (e.g., updating "Milk" to 75)
existing_product = "Milk"
inventory[existing_product] = 75
print(f"\n--- Updated Quantity for '{existing_product}' ---")
print(f"New quantity for {existing_product}: {inventory[existing_product]}")

# Remove one product from the dictionary (e.g., removing "Sugar")
product_to_remove = "Sugar"
del inventory[product_to_remove]
print(f"\n--- Removed Product ('{product_to_remove}') ---")
print(f"'{product_to_remove}' has been successfully removed from inventory.")

# Display the final inventory
print("\n--- Final Inventory ---")
for product, quantity in inventory.items():
    print(f"- {product}: {quantity} units")