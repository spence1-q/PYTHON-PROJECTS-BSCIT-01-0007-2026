# Open customers.txt in read mode (r)
f = open("customers.txt", "r")

# Read the contents of the file
contents = f.read()

# Display the contents on the screen
print("--- Customer Information ---")
print(contents)

# Close the file
f.close()

#r (Read Mode): Opens an existing file strictly for reading data. It raises a FileNotFoundError if the file does not exist, and the file pointer is placed at the beginning of the file.

# w (Write Mode): Opens a file for writing data. If the file already exists, it clears (truncates) the existing content. If the file does not exist, it creates a new file.

# a (Append Mode): Opens a file for writing data, but places the file pointer at the end of the file so new data is added without deleting existing content. If the file does not exist, it creates a new file.