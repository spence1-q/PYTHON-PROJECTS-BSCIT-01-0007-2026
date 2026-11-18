# Open sales.txt in append mode (a)
f = open("sales.txt", "a")

# Ask the user to enter product name, quantity sold, and total sales amount
product_name = input("Enter product name: ")
quantity_sold = input("Enter quantity sold: ")
total_sales = input("Enter total sales amount: ")

# Write the new sales record to the file
f.write(f"Product: {product_name} | Quantity Sold: {quantity_sold} | Total Sales: {total_sales}\n")

# iv. Close the file
f.close()

#Append mode (a) is ideal for daily sales records because transactions accumulate continuously over time. It ensures that any new sales record entered is added to the end of the file without erasing, overwriting, or losing previous sales history.