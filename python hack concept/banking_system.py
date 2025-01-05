# Creating the banking system!!
class Account:
    def __init__(self, bal):
        self.balance = bal

    # Debited to the account
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs {amount} is debited")
        print(f"Total balance: {self.balance}")

    # Credited to the account
    def credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} is credited")
        print(f"Total balance: {self.balance}")

    def display_balance(self):
        return self.balance
    
acc1 = Account(12000)
acc1.debit(1000)
acc1.credit(500)