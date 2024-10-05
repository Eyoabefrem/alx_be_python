class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Successfully deposited ${amount:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")