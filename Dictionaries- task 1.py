# Create a dictionary named student containing registration number, name, course, and year of study
student = {
    "registration_number": "BSCIT-20-0005/2024",
    "student_name": "cycy",
    "course": "Software Engineering",
    "year_of_study": 1
}

print("--- Initial Student Dictionary ---")
print(student)

# Display the student's name and course using their dictionary keys
print("\n---Displaying Name and Course ---")
print(f"Student Name: {student['student_name']}")
print(f"Course: {student['course']}")

# Change the student's year of study
student["year_of_study"] = 2
print("\n--- Updated Year of Study ---")
print(f"New Year of Study: {student['year_of_study']}")

# Add an email address to the dictionary
student["email"] = "cycy@home.com"
print("\n--- Added Email Address ---")
print(f"Email added: {student['email']}")

# v. Display the complete updated dictionary
print("\n--- Complete Updated Dictionary ---")
print(student)