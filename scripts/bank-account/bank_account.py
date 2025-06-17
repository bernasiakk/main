from random import randint


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

    def get_balance(self):
        return self.balance

    def open(self):
        """
        assign number at this point only??
        or should it just mark the ticker as `opened`? TODO check the tests
            yeah, there is something like this. Just have a `opened` boolean variable
        """
        if self.active:
            raise ValueError("Cannot open an account that's already open")
        self.active = 1
        return self

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if self.balance - amount < 0:
            raise ValueError("Insufficient funds.")
        self.balance = self.balance - amount
        return self

    def close(self):
        if not self.active:
            raise ValueError("Cannot close an inactive account")
        self.active = 0
        return self

# some_acc = BankAccount()
# some_acc.open()
# print(some_acc.get_balance())