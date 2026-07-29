
# 2. Bank Account Deposit/Withdraw
class BankAccount:
    def __init__(self, account_number,holder_name , balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

acc = BankAccount("12345","shainum" ,  1000000)
acc.deposit(500)
acc.withdraw(300)
print("Balance:", acc.balance)

# Balance: 1200 this is the output 
# here we are still going to explain few more things in this we are add still elements 