class BankAccount:

  def __init__(self, account_number="", customer_name="", balance=0.0):
    self.account_number = account_number
    self.customer_name = customer_name
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Successfully deposited Kshs{amount:.2f}. New Balance: Kshs{self.balance:.2f}")
    else:
      print("Deposit amount must be greater than zero.")

  def withdraw(self, amount):
    if amount > 0:
      # Ensure that a customer cannot withdraw more money than the available balance
      if amount <= self.balance:
        self.balance -= amount
        print(f"Successfully withdrew Kshs{amount:.2f}. New Balance: Kshs{self.balance:.2f}")
      else:
        print("Error: Insufficient funds! Cannot withdraw more than available balance.")
    else:
      print("Withdrawal amount must be greater than zero.")

  def display_details(self):
    print(
        f"Account No: {self.account_number} | Customer: {self.customer_name} |"
        f" Balance: Kshs{self.balance:.2f}"
    )


# Use a function named performTransaction() to process a deposit or withdrawal
def performTransaction(account):
  print(f"\nProcessing transaction for: {account.customer_name} (Acc: {account.account_number})")
  print("1. Deposit")
  print("2. Withdrawal")
  choice = input("Enter choice (1 or 2): ")

  if choice == "1":
    while True:
      # Use try...except to handle non-numeric transaction amounts
      try:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
        break
      except ValueError:
        print("Invalid input! Please enter a valid numeric amount.")
  elif choice == "2":
    while True:
      try:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
        break
      except ValueError:
        print("Invalid input! Please enter a valid numeric amount.")
  else:
    print("Invalid choice selected.")


# Create at least two bank account objects
accounts = [
    BankAccount("ACC101", "Obed Ondieki", 2500.00),
    BankAccount("ACC102", "Tonny Nyaribo", 7550.50)
]

print("--- Initial Account Details ---")
for acc in accounts:
  acc.display_details()

# Execute transactions
for acc in accounts:
  performTransaction(acc)

# Display the updated balance for each account
print("\n--- Updated Account Details ---")
for acc in accounts:
  acc.display_details()

# Save the account details and updated balances to a file named accounts.txt and close
file = open("accounts.txt", "w")
for acc in accounts:
  file.write(
      f"Account Number: {acc.account_number}, Customer Name: {acc.customer_name}, Updated Balance: {acc.balance}\n"
  )
file.close()
print("\nAccount details successfully saved to 'accounts.txt'.")