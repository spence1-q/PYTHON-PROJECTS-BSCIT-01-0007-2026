# Ask the user to enter employee name, basic salary, and monthly deduction
emp_name = input("Enter employee name: ")
basic_salary_str = input("Enter basic salary: ")
deduction_str = input("Enter monthly deduction: ")

# Convert the salary and deduction to floating-point numbers
basic_salary = float(basic_salary_str)
deduction = float(deduction_str)

# Calculate the housing allowance (10% of basic salary)
housing_allowance = 0.10 * basic_salary

# Calculate the gross salary
gross_salary = basic_salary + housing_allowance

# Calculate the net salary
net_salary = gross_salary - deduction

# Display the basic salary, allowance, gross salary, deduction, and net salary
print("\n--- Salary Details ---")
print(f"Employee Name: {emp_name}")
print(f"Basic Salary: {basic_salary:.2f}")
print(f"Housing Allowance: {housing_allowance:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")
print(f"Monthly Deduction: {deduction:.2f}")
print(f"Net Salary: {net_salary:.2f}")