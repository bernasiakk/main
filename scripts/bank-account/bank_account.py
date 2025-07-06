from random import randint
from functools import wraps

def require_positive_amount(f):
    @wraps(f)
    def wrapper(self, amount, *args, **kwargs):
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        return f(self, amount, *args, **kwargs)
    return wrapper

def require_active_account(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        if not self.active:
            raise ValueError("account not open")
        return f(self, *args, **kwargs)
    return wrapper

class BankAccount:
    bank_acct_numbers = set()
    
    def __init__(self):
        while True:
            potential_number = randint(1000, 9999)
            if potential_number not in self.bank_acct_numbers:
                self.acct_number = potential_number
                self.bank_acct_numbers.add(potential_number)
                self.active = 0
                break
        self.balance = 0

    @require_active_account
    def get_balance(self):
        return self.balance

    def open(self):
        """
        assign number at this point only??
        or should it just mark the ticker as `opened`? TODO check the tests
            yeah, there is something like this. Just have a `opened` boolean variable
        """
        if self.active:
            raise ValueError("account already open")
        self.active = 1
        return self

    @require_active_account
    @require_positive_amount
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    @require_active_account
    @require_positive_amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("amount must be less than balance")
        self.balance = self.balance - amount
        return self

    @require_active_account
    def close(self):
        self.active = 0
        self.balance = 0
        return self

# some_acc = BankAccount()
# some_acc.open()
# print(some_acc.get_balance())