# Ask the user to enter student name, coursework mark (out of 30), and examination mark (out of 70)
student_name = input("Enter student name: ")
coursework_mark = float(input("Enter coursework mark (out of 30): "))
examination_mark = float(input("Enter examination mark (out of 70): "))

# Calculate the total mark
total_mark = coursework_mark + examination_mark

# Use comparison operators to determine whether the student has achieved at least 40 marks
has_passed = total_mark >= 40

# Display the student's name, coursework mark, examination mark, and total mark
print("\n--- Student Result Summary ---")
print(f"Student Name: {student_name}")
print(f"Coursework Mark: {coursework_mark}")
print(f"Examination Mark: {examination_mark}")
print(f"Total Mark: {total_mark}")

# Display True or False to indicate whether the student has passed
print(f"Has Passed (>= 40): {has_passed}")