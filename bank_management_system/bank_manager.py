from user import UserManager
from accounts import AccountManager, CurrentAccount, SavingsAccount
from transactions import TransactionManager
from log_service import app_logger

class BankManager:        
    def __init__(self, db):
        self.__db = db
        self.user_manager = UserManager(self.__db)
        self.account_manager = AccountManager(self.__db)
        self.transaction = TransactionManager(self.__db)

    def new_account(self, name, address, phone_no, email, dob, gender):
        if not phone_no or not name:
            app_logger.log('warning', 'Some required fields are not filled!')
            print("Somre required fields are not filled!")
            name = input("Enter name:")
            phone_no = input("Enter phone number:")

        user_id = self.user_manager.create_user(name=name,address=address,phone_no=phone_no, email=email, dob=dob, gender=gender)
        if user_id:
            app_logger.log('info', f'Profile created successfully for user:{user_id}')
            print("\nProfile created successfully!\nProvide account details:")
            account_type = self.get_account_type()
            
            pin = input("Set your PIN (4 digits): ")

            self.account_manager.create_account(user_id, account_type, pin)
            app_logger.log('info', f'Account created successfully for user {user_id} with account type {account_type}')
            print("Account created successfully!")
        else:
            app_logger.log('error', f"Error creating user account for {name}")
            print("Error creating user account.")
    
    def get_account_type(self):
        """Function to handle account type selection with validation."""
        while True:
            print("\nSelect Account Type:")
            print("1. Savings")
            print("2. Current")
            print("3. Salary")
            
            try:
                account_choice = int(input("Enter your choice (1, 2, or 3): "))
                if account_choice == 1:
                    app_logger.log('info', 'User selected Savings account type')
                    return "Savings"
                elif account_choice == 2:
                    app_logger.log('info', 'User selected Current account type')
                    return "Current"
                elif account_choice == 3:
                    app_logger.log('info', 'User selected Salary account type')
                    return "Salary"
                else:
                    print("Invalid option. Please choose a valid account type.")
                    app_logger.log('warning', 'User entered invalid account type choice')
            except ValueError:
                print("Invalid input! Please enter a number (1, 2, or 3).")
                app_logger.log('warning', 'User entered invalid input for account type')
    
    def get_account_manager(self, account_type):
        """Returns the correct AccountManager subclass (Current or Savings) based on account_type."""
        if account_type == "Savings":
            return SavingsAccount(self.db)  # You should pass any required parameters here, like db, balance, etc.
        elif account_type == "Current":
            return CurrentAccount(self.db)
        else:
            raise ValueError("Unknown account type")

    def check_balance(self):
        
        account_number = input("Enter your account number: ")

        pin = input("Enter your PIN: ")

        account_details = self.account_manager.get_account(account_number, pin)
        if not account_details:
            app_logger.log('warning', f"Account not found for account_number {account_number}")
            print("Account not found!")
            return
        app_logger.log('info', f"Checked balance for account_number {account_number}, balance: {float(account_details['balance'])}")
        print(f"Current balance: {float(account_details['balance'])}")        


    def deposit(self):
        account_no = input("Enter account number:")
        pin = input("Enter 4-digit pin:")
        account_details = self.account_manager.get_account(account_no, pin)
        if account_details:
            amount = float(input("Enter the amount:"))
            if amount <=0:
                app_logger.log('warning', f"Invalid deposit amount entered for account {account_no}")
                print("Amount must be greater than Rs 0")
                return
            self.account_manager.deposit_amount(account_details['account_id'], amount)
            app_logger.log('info', f"Deposited Rs {amount} to account {account_no}")
        else:
            app_logger.log('error', f"Account {account_no} not found for deposit")
            print("Account Not Found!")    
    
    def withdraw(self):
        account_number = input("Enter account number: ")
        pin = input("Enter your PIN: ")

        # Get account details and determine the account type
        account_details = self.account_manager.get_account(account_number, pin)
        if not account_details:
            app_logger.log('error', f"Invalid account number or PIN for account {account_number}")
            print("Invalid account number or PIN.")
            return

        account_type = account_details["account_type"]
        account_id = account_details["account_id"]
        amount = input("Enter withdrawal amount: ")

        # Dynamically instantiate the correct account type subclass
        if account_type == "Current":
            app_logger.log('info', f"Withdrawing Rs {amount} from Current account {account_number}")
            current_account = CurrentAccount(self.db, account_id=account_id, balance=0, user_id=account_id)
            current_account.withdraw_amount(account_id,amount)
            
        elif account_type == "Savings":
            app_logger.log('info', f"Withdrawing Rs {amount} from Savings account {account_number}")
            savings_account = SavingsAccount(self.db, account_id=account_id, balance=0, user_id=account_id)
            savings_account.withdraw_amount(account_id, amount)
            
        else:
            app_logger.log('error', f"Invalid account type for withdrawal: {account_type} for account {account_number}")
            print("Invalid account type. Please try again.")

    def get_history(self):

        account_number = input("Enter account number: ")
        pin = input("Enter your PIN: ")

        # Get account details and determine the account type
        account_details = self.account_manager.get_account(account_number, pin)
        if not account_details:
            app_logger.log('error', f"Invalid account number or PIN for account {account_number}")
            print("Invalid account number or PIN.")
            return

        account_id = account_details["account_id"]
        self.transaction.transaction_history(account_id, account_number)
        app_logger.log('info', f"Retrieved transaction history for account {account_number}")
    
    def account_info(self):
        account_no = input("Enter account no:")
        self.account_manager.display_account_details(account_no)

    def transfer(self):
        """Transfer amount from one account to another."""
        try:
            sender_account_number = input("Enter your account number: ")
            sender_pin = input("Enter your PIN: ")
            app_logger.log('info', f"Transfer initiated from account {sender_account_number}")
            
            sender_details = self.account_manager.get_account(sender_account_number, sender_pin)
            if not sender_details:
                app_logger.log('warning', f"Invalid sender account or PIN for account {sender_account_number}")
                print("Invalid sender account number or PIN.")
                return

            to_account_number = input("Enter receiver's account number: ")
            app_logger.log('info', f"Receiver account number: {to_account_number}")
            # Validate receiver's account details
            receiver_details = self.account_manager.check_account_exists(to_account_number)  # Same PIN check for simplicity, but typically separate
            if not receiver_details:
                app_logger.log('warning', f"Invalid receiver account number {to_account_number}")
                print("Invalid receiver account number.")
                return

            sender_account_id = sender_details['account_id']
            sender_account_type = sender_details["account_type"]
            sender_balance = sender_details['balance']

            receiver_account_id = receiver_details['account_id']

            # Get transfer amount
            amount = float(input("Enter the amount to transfer: "))

            app_logger.log('info', f"Amount to transfer: {amount}")
            if amount <= 0:
                app_logger.log('warning', f"Invalid transfer amount {amount} for account {sender_account_number}")
                print("Amount must be greater than zero.")
                return

            # Check if sender has enough balance
            if amount > sender_balance:
                app_logger.log('warning', f"Insufficient funds in sender account {sender_account_number}. Available balance: {sender_balance}")
                print("Insufficient funds in sender's account.")
                return
            success_msg = self.account_manager.transfer_amount(sender_account_id, receiver_account_id, amount, sender_account_number, to_account_number)
            app_logger.log('info', f"Successfully transferred {amount} from account {sender_account_number} to account {to_account_number}")
            print(success_msg)
        except Exception as e:
            app_logger.log('error', f"Error during transfer: {e}")
            print(f"An error occurred: {e}")


