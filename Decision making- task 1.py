# Ask the student to enter their name and mark, then convert mark to an integer
student_name = input("Enter student's name: ")
mark = int (input("Enter examination mark: "))

# Check if the mark is out of valid bounds (below 0 or above 100)
if mark < 0 or mark > 100:
    print("Invalid mark")
else:
    # Use an if...elif...else statement to assign grades
    if mark >= 70:
        grade = "A"
    elif mark >= 60:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    elif mark >= 40:
        grade = "D"
    else:
        grade = "F"
    
    # Display the student's name, mark, and grade
    print(f"\nStudent Name: {student_name}")
    print(f"Mark: {mark}")
    print(f"Grade: {grade}")