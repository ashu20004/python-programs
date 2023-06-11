# Create a BankAccount class. Your class should support the following methods:
# a. __init__(self, account_no)
# b. deposit (self, account_no, amount)c. withdraw (self, account_no, amount)
# d. get_balance (self, account_no)

class BankAccount:
    def __init__(self, account_no):
        self.account_no = account_no
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to Account {self.account_no}.")
        else:
            print("Invalid amount. Deposit amount should be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from Account {self.account_no}.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance


account = BankAccount("123456")

account.deposit(1000)

account.withdraw(500)


balance = account.get_balance()
print(f"Current balance of Account {account.account_no}: {balance}")
