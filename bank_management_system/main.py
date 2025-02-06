from db_connection import Database
from bank_manager import BankManager
from utils import Validators
import constants        
from log_service import app_logger

print ("--------------Welcome to MyBank!--------------")
print("\nPlease select to option\n------------------\n")
print("1. Create Account\n2. Deposit Amount\n3. Withdraw Amount\n4. Check Balance\n5. Transaction History\n6. Account Info\n7. Transfer Amount to another Account\n")
choice = int(input("Enter your option:"))
db = Database()  
bank_manager = BankManager(db)  
validator = Validators()
valid_input = True

match choice:
    case 1:
        app_logger.log('info', "User selected option 1: Create Account")
        name = input("Enter your name: ")
        address = input("Enter your address: ")
        email = input('Enter your email:')
        
        phone_no = input("Enter your phone number: ")
        
        dob = input("Enter date of birth(MM-DD-YYYY):")
        
        gender = input('Enter your gender(M/F):')
        if not validator.validate_email(email):
            app_logger.log('warning', 'Invalid email entered')
            print("Invalid email. Please enter a valid email address.")
            valid_input = False
        if not validator.validate_phoneno(phone_no):
            app_logger.log('warning', 'Invalid phone no entered')
            print("Invalid phone number. Please enter a 10-digit number.")
            valid_input = False
        if not validator.validate_dob(dob):
            app_logger.log('warning', 'Invalid date of birth entered')
            print("Invalid Date of Birth. Please enter in MM-DD-YYYY format.")
            valid_input = False 
        if not validator.validate_gender(gender):
            app_logger.log('warning', 'Invalid gender entered')
            print("Invalid gender. Please enter 'M' for male or 'F' for female.")
            valid_input = False
        if valid_input:
            app_logger.log('info','Details received. Creating Account')
            bank_manager.new_account(name=name, address=address, phone_no=phone_no,email=email, dob=dob, gender=gender)
        else:
            app_logger.log('error', 'Invalid account details')
            print(constants.INVALID_ACC_DETAILS_MSG)
    case 2: 
        app_logger.log('info', "User selected option 2: Deposit Amount")
        bank_manager.deposit()
    case 3:
        app_logger.log('info', "User selected option 3: Withdraw Amount")
        bank_manager.withdraw()
    case 4:
        app_logger.log('info', "User selected option 4: Check Balance")
        bank_manager.check_balance()
    case 5:
        app_logger.log('info', "User selected option 5: Get History")
        bank_manager.get_history()
    case 6:
        app_logger.log('info', "User selected option 6: Account Info")
        bank_manager.account_info()
    case 7:
        app_logger.log('info', "User selected option 7: Transfer Amount to another Account")
        bank_manager.transfer()
    case _:
        app_logger.log('warning', "User selected option invalid option")
        print("Invalid choice!")
    

