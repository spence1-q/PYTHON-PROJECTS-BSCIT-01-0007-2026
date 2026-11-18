try:
    #  Ask the customer to enter the withdrawal amount & 
    #  Convert to int inside try block
    amount = int(input("Enter the amount you want to withdraw: "))
    
    # Display the withdrawal amount when a valid number is entered
    print(f"Withdrawal amount: {amount}")

except ValueError:
    #  Use except block to handle ValueError and display the required message
    print("Invalid amount. Please enter a number.")