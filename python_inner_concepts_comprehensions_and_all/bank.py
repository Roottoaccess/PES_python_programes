# balance = 0

# def deposit(x): # Using the global variable
#     global balance 
#     balance += x; return balance

# def withdraw(x):
#     global balance
#     balance -= x; return balance

# def main():
#     deposit(100)
#     print(f"Balance: {balance}")
#     withdraw(50)
#     print(f"Balance: {balance}")

# if __name__ == "__main__":
#     main()

class Account: # Using the OOPS concept
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:",account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:",account.balance)

if __name__ == "__main__":
    main()

