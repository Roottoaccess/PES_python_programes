# This is the project using oops
# Banking system

class Bank_Account: # Created the bank class !!
    def __init__(self, account_number, balance):
        self.acc_no = account_number
        self.balance = balance

    # Creating a static method
    @staticmethod
    def greeting():
        print("Welcome to the bank portal !")

    # For debiting the balance from the account
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs {amount} is been debited !")
        print(f"Total balance {self.balance}")

    # For credited the balance from the account
    def credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} is been credited !")
        print(f"Total balance {self.balance}")

    def show_balance(self):
        return self.balance
    
# Creating the object for the class
obj = Bank_Account(12344, 12000)
obj.greeting()
obj.debit(500)
obj.credit(1000)
obj.show_balance