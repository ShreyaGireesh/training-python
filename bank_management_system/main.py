from db_connection import Database
from bank_manager import BankManager
        

print ("--------------Welcome to MyBank!--------------")
print("\nPlease select to option\n------------------\n")
print("1. Create Account\n2. Deposit Amount\n3. Withdraw Amount\n4. Check Balance\n5. Transaction History\n")
choice = int(input("Enter your option:"))
db = Database()  
bank_manager = BankManager(db)  
match choice:
    case 1:
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        phone_no = input("Enter your phone number: ")
        bank_manager.new_account(name, address, phone_no)
    case 2:
        bank_manager.deposit()
    case 3:
        bank_manager.withdraw()
    case 4:
        bank_manager.check_balance()
    

