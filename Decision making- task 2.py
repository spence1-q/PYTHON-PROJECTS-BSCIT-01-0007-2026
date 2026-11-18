# Store the initial account balance as KSh 50,000
account_balance = 50000

# Ask the customer to enter the withdrawal amount and convert it to an integer
withdrawal_amount = int(input("Enter withdrawal amount (KSh): "))

# Check the withdrawal conditions
if withdrawal_amount <= 0:
    print("Error: Withdrawal amount must be greater than zero.")
elif withdrawal_amount > account_balance:
    print("Error: Withdrawal amount exceeds the account balance.")
elif withdrawal_amount % 500 != 0:
    print("Error: Withdrawal amount must be a multiple of KSh 500.")
else:
    #  Deduct the amount from the balance if all conditions are satisfied
    account_balance -= withdrawal_amount
    
    #  Display the remaining balance
    print(f"Withdrawal successful. Remaining balance: KSh {account_balance}")