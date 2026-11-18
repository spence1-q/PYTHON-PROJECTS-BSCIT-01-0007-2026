# Open a file named students.txt in write mode (w)
f = open("students.txt", "w")

# Write information for at least three students using print(..., file=f)
# Student 1
print("Student Name: Obed Ondieki", file=f)
print("Registration Number: BSCIT-50-0001/2024", file=f)
print("Course: Information Technology", file=f)
print("Mark: 85", file=f)
print("-" * 30, file=f)

# Student 2
print("Student Name: Brian Duke", file=f)
print("Registration Number: BSE-05-0002/2024", file=f)
print("Course: Software Engineering", file=f)
print("Mark: 78", file=f)
print("-" * 30, file=f)

# Student 3
print("Student Name: Newton Mwangi", file=f)
print("Registration Number: BCS-05-0003/2024", file=f)
print("Course: Computer Science", file=f)
print("Mark: 92", file=f)
print("-" * 30, file=f)

# Close the file using close()
f.close()

#If the file students.txt already exists, opening it in write mode (w) will truncate (overwrite) all existing contents, clearing the file completely before writing the new data. If the file does not exist, Python will create a new file.