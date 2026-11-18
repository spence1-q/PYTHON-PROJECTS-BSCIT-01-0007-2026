# Create variables and assign suitable values
emp_name = "Newton Ondieki"
emp_age = 26
emp_salary = 75000.50
is_active = True  # Store active status using a Boolean value

# Display all employee information using f-string formatting
print("--- Employee Details ---")
print(f"Name: {emp_name}")
print(f"Age: {emp_age}")
print(f"Salary: ${emp_salary}")
print(f"Active Status: {is_active}")

# Demonstrate how a number can be converted to a string using str() before concatenation
age_message = "Employee age is " + str(emp_age) + " years old."
print(age_message)