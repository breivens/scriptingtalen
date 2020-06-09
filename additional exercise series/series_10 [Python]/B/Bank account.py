class BankAccount:
    def __init__(self, holder: str, number: str, amount=0):
        self.holder, self.number, self.account = holder, number, amount

    def __str__(self):
        return f'{self.holder}, {self.number}, amount: {self.account}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.holder!r}, {self.number!r}, {self.account})'

    def deposit(self, amount):
        self.account += amount

    def withdraw(self, amount):
        self.account -= amount
