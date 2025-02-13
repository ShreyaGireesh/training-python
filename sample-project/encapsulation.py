# Bank account, where user can deposit and withdraw amount and can only view their balance
class Bank:
    """ 
    A class for managing bank deposit, withdrawal and to get balance.
    Attributes
    name(str): the name of account holder
    __balance: To get balance. A private attribute.

    Methods
    deposit(): to deposit an amount
    withdraw(): to withdraw amount
    getbalance(): to view the current balance
    """
    bank_name = "MyBank"
    def __init__(self, name):
        self.name = name
        self.__balance = 0

    def deposit(self,amount):
        self.__balance+=amount
        return f"Deposited Rs.{amount} by {self.name}. Current balance: Rs{self.__balance}"
    
    def withdrawal(self,amount):
        if ((self.__balance -self.amount)< 0):
            return f"Withdrawal cancelled!"
        self.__balance-=amount
        return f"Withdrawed Rs.{amount} by {self.name}. Current balance: Rs{self.__balance}"

    def getbalance(self):
        return f"Current Balance: {self.__balance}"

    @staticmethod
    def bank_info():
        return f"Welcome to {Bank.bank_name}"

name = input("Enter name:")
person = Bank(name)
print(person.bank_info())

print("Select your option:\n----------------\n1. Deposit Amount\n2. Withdraw Amount\n3. Check Balance")
choice = int(input("Enter your option:"))
match choice:
    case 1:
        amount = int(input("Enter Amount:"))
        print(person.deposit(amount))
    case 2:
        amount = int(input("Enter Amount:"))
        print(person.withdraw(amount))
    case 3:
        print(person.getbalance())

print(person._Bank__balance)
