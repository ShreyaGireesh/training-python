from user import UserManager
from accounts import AccountManager, CurrentAccount, SavingsAccount

class BankManager:        
    def __init__(self, db):
        self.db = db
        self.user_manager = UserManager(self.db)
        self.account_manager = AccountManager(self.db)

    def new_account(self, name, address, phone_no):
        if not phone_no or not name:
            print("Somre required fields are not filled!")
            name = input("Enter name:")
            phone_no = input("Enter phone number:")

        user_id = self.user_manager.create_user(name=name,address=address,phone_no=phone_no)
        if user_id:
            print("\nProfile created successfully!\nProvide account details:")
            account_type = self.get_account_type()
            
            pin = input("Set your PIN (4 digits): ")

            self.account_manager.create_account(user_id, account_type, pin)
            
            print("Account created successfully!")
        else:
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
                    return "Savings"
                elif account_choice == 2:
                    return "Current"
                elif account_choice == 3:
                    return "Salary"
                else:
                    print("Invalid option. Please choose a valid account type.")
            except ValueError:
                print("Invalid input! Please enter a number (1, 2, or 3).")
    
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
            print("Account not found!")
            return
        print(f"Current balance: {float(account_details['balance'])}")        


    def deposit(self):
        account_no = input("Enter account number:")
        pin = input("Enter 4-digit pin:")
        account_details = self.account_manager.get_account(account_no, pin)
        if account_details:
            amount = float(input("Enter the amount:"))
            if amount <=0:
                print("Amount must be greater than 0")
                return
            self.account_manager.deposit_amount(account_details['account_id'], amount)

        else:
            print("Account Not Found!")    
    
    def withdraw(self):
        account_number = input("Enter account number: ")
        pin = input("Enter your PIN: ")

        # Get account details and determine the account type
        account_details = self.account_manager.get_account(account_number, pin)
        if not account_details:
            print("Invalid account number or PIN.")
            return

        if not account_details:
            print("Invalid account number or PIN.")
            return

        account_type = account_details["account_type"]
        account_id = account_details["account_id"]
        amount = input("Enter withdrawal amount: ")

        # Dynamically instantiate the correct account type subclass
        if account_type == "Current":
            current_account = CurrentAccount(self.db, account_id=account_id, balance=0, user_id=account_id)
            current_account.withdraw_amount(account_id,amount)
        elif account_type == "Savings":
            savings_account = SavingsAccount(self.db, account_id=account_id, balance=0, user_id=account_id)
            savings_account.withdraw_amount(account_id, amount)
        else:
            print("Invalid account type. Please try again.")

    # def get_history(self):

    #     account_number = input("Enter account number: ")
    #     pin = input("Enter your PIN: ")

    #     # Get account details and determine the account type
    #     account_details = self.account_manager.get_account(account_number, pin)
    #     if not account_details:
    #         print("Invalid account number or PIN.")
    #         return

    #     account_id = account_details["account_id"]
