try:
    # Ask the student to enter their age and convert to an integer
    age = int(input("Enter your age: "))
    
    # Display success message if a valid number is entered
    print("Age successfully recorded")

except ValueError:
    # Use except block to handle invalid input (e.g., "twenty") and display message
    print("Invalid age entered")