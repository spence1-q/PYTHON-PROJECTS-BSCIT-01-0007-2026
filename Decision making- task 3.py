# Ask the employee to enter their details
employee_name = input("Enter employee name: ")
years_str = input("Enter years of service: ")
rating_str = input("Enter performance rating: ")

# Convert the years of service and performance rating to integers
years_of_service = int(years_str)
performance_rating = int(rating_str)

# Use logical operators to check eligibility
# Checks if years of service is at least 3 AND performance rating is at least 4
is_eligible = (years_of_service >= 3) and (performance_rating >= 4)

# Determine the eligibility message
if is_eligible:
    status_message = "Employee qualifies for a bonus"
else:
    status_message = "Employee does not qualify for a bonus"

# Display the employee's details and eligibility result
print("\n--- Employee Eligibility Report ---")
print(f"Employee Name: {employee_name}")
print(f"Years of Service: {years_of_service}")
print(f"Performance Rating: {performance_rating}")
print(f"Status: {status_message}")