# Accept employee details from the keyboard
emp_name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
emp_age_input = input("Enter employee age: ")
emp_salary_input = input("Enter basic salary: ")

#  Convert age to an integer and basic salary to a floating-point number
emp_age = int(emp_age_input)
basic_salary = float(emp_salary_input)

#  Calculate the annual salary
annual_salary = basic_salary * 12

# Display employee details using an f-string with salary values to two decimal places
print("\n--- Employee Information ---")
print(f"Employee Name: {emp_name}")
print(f"Employee ID: {emp_id}")
print(f"Employee Age: {emp_age}")
print(f"Basic Salary: ${basic_salary:.2f}")
print(f"Annual Salary: ${annual_salary:.2f}")