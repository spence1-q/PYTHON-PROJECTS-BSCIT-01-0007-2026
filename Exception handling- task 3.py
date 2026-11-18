try:
    # Use a try block to open employees.txt in read mode
    file = open("employees.txt", "r")
    
    # Read and display the contents of the file
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    # Use an except FileNotFoundError block to display the required message
    print("The employee file was not found.")

finally:
    # Use a finally block to display completion message
    print("File processing completed.")