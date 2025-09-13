# The below example shows a BankAccount class with both class and instance attributes
# class BankAccount:
#     total_accounts = 0  # Class attribute: Shared by ALL accounts
#     total_balance = 0  # Class attribute: Tracks bank's total money

#     def __init__(self, name: str, balance: float):
#         self.name = name  # Instance: Each account has unique owner
#         self.balance = balance  # Instance: Each account has unique balance
#         BankAccount.total_accounts += 1
#         BankAccount.total_balance += balance


# 1. We use class attributes to track bank-wide information that is shared by all accounts, such as total # of accs and total balance of accs
# 2. We use instance attrbutes to track account-specific info that is unique to each account, such as each acc's balance and owner.


# CHALLENGE: Implement a BankAccount class that effectively uses both class and instance attrbutes.
# The attributes you need to track are:
#   The total number of accounts in bank [total_accounts]
#   The bank's total balance [total_balance]
#   The individual account owner's name [name]
#   The individual account balance [balance]

# Your tasks are:
#   1. Decide which attributes should be class vs instance attributes
#   2. Implement the BankAccount class
#   3. Create two accounts, "Alice" and "Bob" with balances 1000 and 2000 respectively
#   4. Print the information using the following format:
#       print(f"Alice's balance: <Alice's balance>")
#       print(f"Bob's balance: <Bob's balance>")
#       print(f"Total Accounts: <Total Accounts>")
#       print(f"Total Balance: <Total Balance>")
# UAT/Expected Output:
#   Alice's balance: $1000
#   Bob's balance: $2000
#   Total Accounts: 2
#   Total Balance: $3000


class BankAccount:
    # DONE: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0

    def __init__(self, name=str, balance=int) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
Alice = BankAccount("Alice", 1000)
Bob = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${Alice.balance}")
print(f"Bob's balance: ${Bob.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")
