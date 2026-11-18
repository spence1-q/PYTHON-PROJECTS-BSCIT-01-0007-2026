# Create a dictionary named employees containing at least five employees and their salaries
employees = {
    "Bob Key": 75000,
    "Cappy Jano": 65000,
    "Charlies Obed": 82000,
    "Diana james": 90000,
    "Evan Wamae": 71000
}

print("--- Initial Employees Record ---")
print(employees)

# Display all employee names and salaries using a loop
print("\n---All Employee Names and Salaries ---")
for name, salary in employees.items():
    print(f"Employee: {name} | Salary: ${salary:,.2f}")

# Update the salary of one employee (e.g., Bob Key' salary updated to 70,000)
employee_to_update = "Bob Key"
employees[employee_to_update] = 70000
print(f"\n---  Updated Salary for '{employee_to_update}' ---")
print(f"{employee_to_update}'s new salary: ${employees[employee_to_update]:,.2f}")

# Add a new employee and salary
new_employee = "Yobra Mkuu"
new_salary = 79000
employees[new_employee] = new_salary
print(f"\n---Added New Employee ({new_employee}) ---")
print(f"Added {new_employee} with salary ${new_salary:,.2f}")

# Calculate and display the total salary payable to all employees
total_salary = sum(employees.values())
print(f"\n---Total Salary Payable ---")
print(f"Total Salary Payable to All Employees: ${total_salary:,.2f}")