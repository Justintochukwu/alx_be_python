class BankAccount: 
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self._balance -= amount
            return True
        return False
    
    def display_balance(self):
        print(f"Current Balance: $ {self._balance:.2f}")