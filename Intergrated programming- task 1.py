class Student:

  def __init__(self, name="", reg_number="", course="", mark=0.0):
    self.name = name
    self.reg_number = reg_number
    self.course = course
    self.mark = mark

  def set_details(self, name, reg_number, course, mark):
    self.name = name
    self.reg_number = reg_number
    self.course = course
    self.mark = mark

  def calculate_grade(self):
    if self.mark >= 70:
      return "A"
    elif self.mark >= 60:
      return "B"
    elif self.mark >= 50:
      return "C"
    elif self.mark >= 40:
      return "D"
    else:
      return "Fail"

  def display_details(self):
    grade = self.calculate_grade()
    print(
        f"Name: {self.name} | Reg No: {self.reg_number} | Course: {self.course}"
        f" | Mark: {self.mark} | Grade: {grade}"
    )


def displayStudents(students_list):
  for student in students_list:
    student.display_details()


# Main Execution
students = []
print("--- Enter Details for 3 Students ---")
for i in range(3):
  print(f"\nStudent {i+1}:")
  name = input("Enter Student Name: ")
  reg_number = input("Enter Registration Number: ")
  course = input("Enter Course: ")

  # Use try...except to handle invalid marks entered by the user
  while True:
    try:
      mark = float(input("Enter Mark (0-100): "))
      if 0 <= mark <= 100:
        break
      else:
        print("Error: Mark must be between 0 and 100.")
    except ValueError:
      print("Invalid input! Please enter a numeric value for the mark.")

  s = Student()
  s.set_details(name, reg_number, course, mark)
  students.append(s)

print("\n--- All Students List ---")
displayStudents(students)

# Save to students.txt and close file
file = open("students.txt", "w")
for student in students:
  grade = student.calculate_grade()
  file.write(
      f"Name: {student.name}, Reg No: {student.reg_number}, Course:"
      f" {student.course}, Mark: {student.mark}, Grade: {grade}\n"
  )
file.close()
print("\nStudent details successfully saved to 'students.txt'.")
