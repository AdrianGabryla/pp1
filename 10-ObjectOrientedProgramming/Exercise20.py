class Bank():
    def __init__(self, bank_account):
        self.bank_account = bank_account
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        elif self.balance < amount:
            return f"Insufficient funds on the account"
    def display(self):
        return f"Bank Account No: {self.bank_account}\nBalance: PLN {self.balance}"

ing = Bank("12 3456 5555 9090 1111 0000 7722")   
print(ing.display())
ing.deposit(25.30)
print(ing.display())
ing.withdraw(31.70)
print(ing.display())
ing.withdraw(14)
print(ing.display())
    