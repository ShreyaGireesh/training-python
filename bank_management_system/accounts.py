
from db_connection import Database
from constants import ONLY_BALANCE_Q,CHECK_ACC_EXISTS_Q, ACCOUNT_CREATION_Q, GET_BALANCE_Q, ACC_NOT_FOUND, GET_ACCOUNT_Q, DEPOSIT_AMOUNT_Q, WITHDRAW_AMT_Q, SUCCESS_AMT_DEPOSIT, UPDATE_BALANCE_Q
import mysql.connector
from decimal import Decimal
from transactions import TransactionManager
from log_service import app_logger


class AccountManager():
    """
    A class to manage various operations related to bank accounts such as 
    account creation, balance retrieval, deposits, withdrawals, and account transfers.
    """
    def __init__(self, db):
        """
        Initializes the AccountManager with the given database connection.
        
        Args:
            db (Database): The database connection object used to interact with the MySQL database.
        """
        self.__db = db
        self.transaction_manager = TransactionManager(db)
    

    def __generate_accountno(self):
        """
        Generates a new account number by finding the maximum account ID and 
        incrementing it by 1.

        Returns:
            str: The newly generated account number in the format "ACCxxxxxxx".
        """
        self.__db.cursor.execute("SELECT MAX(account_id) FROM accounts")
        max_account_id = self.__db.cursor.fetchone()[0]
        new_account_id = max_account_id + 1 if max_account_id is not None else 1
        app_logger.log('info', f"Generated new account number: ACC{new_account_id:07d}")
        return f"ACC{new_account_id:07d}"

    def create_account(self, user_id, account_type, pin):
        """
        Creates a new account for the user by inserting the details into the database.

        Args:
            user_id (str): The ID of the user.
            account_type (str): The type of account (e.g., "current", "savings").
            pin (str): The pin associated with the account.

        Returns:
            None: Returns None in case of error, otherwise prints account details.
        """
        try:
            self.__db.connection.start_transaction()
            account_number = self.__generate_accountno()
            values=(account_number, user_id, pin, account_type)
            self.__db.cursor.execute(ACCOUNT_CREATION_Q, values)
            self.__db.connection.commit()
            self.display_account_details(account_number)
            app_logger.log('info', f"Successfully created {account_type} account for user {user_id}, Account number: {account_number}")
        except mysql.connector.Error as err:
            app_logger.log('error', f"Error while creating account for user {user_id}: {err}")
            print(f"Error while creating user: {err}")
            self.db.connection.rollback()
            return None 
    
    def display_account_details(self, account_number):
        """
        Fetches and displays the account details in a formatted way.

        Args:
            account_number (str): The account number whose details are to be fetched and displayed.

        Returns:
            None
        """
        try:
            
            self.__db.cursor.execute(
                "SELECT a.account_number, a.account_type, a.balance, u.user_id, u.user_name, u.phone_no, u.address, u.email, u.dob, u.gender "
                "FROM accounts a "
                "JOIN users u ON a.user_id = u.user_id "
                "WHERE a.account_number = %s", 
                (account_number,)
            )
            account_details = self.__db.cursor.fetchone()

            if account_details:
                app_logger.log('info', f"Fetched account details for {account_number}")
                account_number, account_type, balance, user_id, name, phone_no, address, email,dob, gender = account_details

                # Print the account details in a creative format
                print("\n" + "*" * 50)
                print(f"** Account Details **")
                print("*" * 50)
                print(f"Account Number: {account_number}")
                print(f"Account Type: {account_type}")
                print(f"Balance: {Decimal(balance):,.2f}")
                print(f"User Name: {name}")
                print(f"Phone No: {phone_no}")

                print(f"Address: {address if address else 'Not Provided'}")
                print(f"Email: {email if email else 'Not Provided'}")
                print(f"DOB: {dob if dob else 'Not Provided'}")
                print(f"Gender: {gender if gender else 'Not Provided'}")

                print("*" * 50)
            else:
                app_logger.log('warning', f"Account {account_number} not found.")
                print(ACC_NOT_FOUND)

        except mysql.connector.Error as err:
            app_logger.log('error', f"Error while fetching account details for {account_number}: {err}")
            print(f"Error while fetching account details: {err}")

    def get_balance(self, account_number, pin):
        """
        Fetches the balance for a given account number and pin.

        Args:
            account_number (str): The account number.
            pin (str): The pin for verification.

        Returns:
            str: A message with the current balance or an error message if account number or pin is invalid.
        """
        try:
            
            values = (account_number, pin)
            self.__db.cursor.execute(GET_BALANCE_Q, values)
            result = self.__db.cursor.fetchone()

            if result:
                balance = result[0]
                app_logger.log('info', f"Fetched balance for account {account_number}: Rs.{balance:.2f}")
                return f"Your balance is: Rs.{balance:.2f}"
            else:
                app_logger.log('warning', f"Invalid account number or PIN for {account_number}")
                return "Invalid account number or PIN."

        except mysql.connector.Error as err:
            app_logger.log('error', f"Error while fetching balance for {account_number}: {err}")
            print(f"Error while fetching balance: {err}")
            return None

    def get_account(self, account_number, pin):
        """
        Fetches account details based on the account number and pin.

        Args:
            account_number (str): The account number.
            pin (str): The pin for verification.

        Returns:
            dict: A dictionary with account details or None if the account or pin is invalid.
        """
        try:
            
            values = (account_number, pin)
            self.__db.cursor.execute(GET_ACCOUNT_Q, values)
            result = self.__db.cursor.fetchone()
            if result:
                account_id, account_type, balance = result
                app_logger.log('info', f"Fetched account details for account {account_number}: {account_type}, Balance: Rs.{balance:.2f}")
                return {"account_id": account_id, "account_type": account_type, "balance": balance}  
            else:
                app_logger.log('warning', f"Invalid account number or PIN for {account_number}")
                return None
        except mysql.connector.Error as err:
            app_logger.log('error', f"Error while fetching account {account_number}: {err}")
            print(f"Error while fetching balance: {err}")
            return None

    def deposit_amount(self, account_id, amount):
        """
        Deposits a specified amount into the account.

        Args:
            account_id (str): The account ID where the deposit will be made.
            amount (Decimal): The amount to deposit.

        Returns:
            None
        """

        try:
            
            values = (account_id,)
            self.__db.cursor.execute(DEPOSIT_AMOUNT_Q, values)
            current_balance = self.__db.cursor.fetchone()

            new_balance = current_balance[0] + Decimal(amount)
            self.__db.cursor.execute("UPDATE accounts SET balance = %s WHERE account_id =%s",(new_balance, account_id))
            self.__db.connection.commit() 
            self.transaction_manager.add_transaction(account_id=account_id, amount=amount,balance_after=new_balance, transaction_type="deposit", description="Amount deposited")
            app_logger.log('info', f"Deposited Rs {amount} to account ID {account_id}. New balance: Rs.{new_balance:.2f}")
            print(SUCCESS_AMT_DEPOSIT)
        except mysql.connector.Error as err:
            app_logger.log('error', f"Error while depositing amount to account {account_id}: {err}")
            print(f"Error while creating user: {err}")
            self.__db.connection.rollback()
            return None 

    def update_balance(self, account_id, balance):
        """
        Updates the balance of a specified account.

        Args:
            account_id (str): The account ID whose balance will be updated.
            balance (Decimal): The new balance to set.

        Returns:
            bool: True if the balance update is successful, otherwise False.
        """
        try:
            
            values = (balance, account_id)
            self.__db.cursor.execute(UPDATE_BALANCE_Q, values)
            self.__db.connection.commit()
            app_logger.log('info', f"Updated balance for account ID {account_id} to Rs.{balance:.2f}")
        except mysql.connector.Error as err:
            app_logger.log('error', f"Error updating balance for account ID {account_id}: {err}")
            print(f"Error updating balance: {err}")
            self.__db.connection.rollback()
            return False
        return True
    
      
    def check_account_exists(self, account_number):
        """
        Checks if an account exists in the database.

        Args:
            account_number (str): The account number to check.

        Returns:
            dict: A dictionary with account details (account_id, account_type) if the account exists, otherwise None.
        """
        try:
            app_logger.log('info', f"Attempting to fetch account details for account {account_number}")
            values = (account_number,)
            self.__db.cursor.execute(CHECK_ACC_EXISTS_Q, values)
            result = self.__db.cursor.fetchone()
            if result:

                app_logger.log('info', f"Fetched account details for account {account_number}")
                account_id, account_type, balance = result
                return {"account_id": account_id, "account_type": account_type}  # returning account_id and account_type
            else:
                app_logger.log('warning', f"Invalid account number or PIN for {account_number}")
                return None
        except mysql.connector.Error as err:
            app_logger.log('error', f"Error while fetching account {account_number}: {err}")
            print(f"Error while fetching balance: {err}")
            return None

    def transfer_amount(self, sender, receiver, amount, sender_account_number, receiver_account_number):
        """
        Transfers an amount from the sender's account to the receiver's account.

        Args:
            sender (str): The sender's account ID.
            receiver (str): The receiver's account ID.
            amount (Decimal): The amount to transfer.
            sender_account_number (str): The sender's account number.
            receiver_account_number (str): The receiver's account number.

        Returns:
            str: A success message if the transfer is successful, otherwise an error message.
        """
        try:
            app_logger.log('info', f"Fetching balance for sender account {sender_account_number}")
            
            values = (sender,)
            self.__db.cursor.execute(ONLY_BALANCE_Q , values)
            result = self.__db.cursor.fetchone()
            sender_balance = result[0] - Decimal(amount)
            self.update_balance(sender,sender_balance)
            app_logger.log('info', f"Sender account {sender_account_number} balance updated to {sender_balance}")
            self.transaction_manager.add_transaction(account_id=sender, amount=amount, 
                                                     balance_after=sender_balance, 
                                                     transaction_type="transfer", 
                                                     description=f"Amount transferred to {receiver_account_number}",
                                                     transaction_id_related = receiver)
            app_logger.log('info', f"Transaction for sender account {sender_account_number} added successfully.")
            app_logger.log('info', f"Fetching balance for receiver account {receiver_account_number}")
            
            values = (receiver,)
            self.__db.cursor.execute(ONLY_BALANCE_Q , values)
            result = self.__db.cursor.fetchone()
            receiver_balance = result[0] + Decimal(amount)
            self.update_balance(receiver,receiver_balance)
            app_logger.log('info', f"Receiver account {receiver_account_number} balance updated to {receiver_balance}")
            return f"Transfer of {amount} from {sender_account_number} to {receiver_account_number} was successful!"

        except Exception as e:
            app_logger.log('error', f"Unexpected error during transfer from {sender_account_number} to {receiver_account_number}: {e}")
            print(f"Unexpected Logging Error: {e}")
            

class CurrentAccount(AccountManager):
    """
    A class for managing current account-specific operations, inheriting from AccountManager.
    """
    def __init__(self, db, account_id, balance, user_id):
        """
        Initializes the current account with its specific details.

        Args:
            db (Database): The database connection object.
            account_id (str): The account ID.
            balance (Decimal): The current balance.
            user_id (str): The user ID to which the account belongs.
        """
        super().__init__(db)
        self.account_id = account_id
        self.balance = balance
        self.user_id = user_id
        self.account_type = "current"

    def withdraw_amount(self,account_id, amount):
        """
        Performs a withdrawal operation for a current account.

        Args:
            account_id (str): The account ID from which to withdraw.
            amount (Decimal): The amount to withdraw.

        Returns:
            bool: True if the withdrawal is successful, otherwise False.
        """
        try:
            
            values = (account_id,)
            self.db.cursor.execute(WITHDRAW_AMT_Q, values)
            current_balance = self.db.cursor.fetchone()

            if not current_balance:
                app_logger.log('error', f"Account ID {account_id} not found during withdrawal attempt.")
                print(ACC_NOT_FOUND)
                return False

            current_balance = Decimal(current_balance[0])
            # if amount > current_balance:
            #     print("Insufficient balance.")
            #     return False
            new_balance = current_balance - Decimal(amount)

            if not self.update_balance(self.account_id, new_balance):
                app_logger.log('error', f"Failed to update balance for account ID {account_id} after withdrawal of Rs {amount}")   
                return False

            self.transaction_manager.add_transaction(account_id=account_id, amount=amount, 
                                                     balance_after=new_balance, 
                                                     transaction_type="withdraw", 
                                                     description="Amount withdrawn from current account")
            app_logger.log('info', f"Withdrawal of Rs {amount} from account ID {account_id}. New balance: Rs.{new_balance:.2f}")
            print(f"Withdrawal successful! New balance: Rs.{new_balance:.2f}")
            return True
        except mysql.connector.Error as err:
            app_logger.log('error', f"Error during withdrawal from account {account_id}: {err}")
            print(f"Error during withdrawal: {err}")
            self.db.connection.rollback()
            return False

class SavingsAccount(AccountManager):
    """
    A class for managing savings account-specific operations, inheriting from AccountManager.
    """
    def __init__(self, db, account_id, balance, user_id):
        """
        Initializes the current account with its specific details.

        Args:
            db (Database): The database connection object.
            account_id (str): The account ID.
            balance (Decimal): The savings balance.
            user_id (str): The user ID to which the account belongs.
        """
        super().__init__(db)
        self.account_id = account_id
        self.balance = balance
        self.user_id = user_id
        self.account_type = "savings"
        self.__limit = Decimal(100)
    
    def withdraw_amount(self, account_id, amount):

        """
        Performs a withdrawal operation for a savings account after checking minimum balance.

        Args:
            account_id (str): The account ID from which to withdraw.
            amount (Decimal): The amount to withdraw.

        Returns:
            bool: True if the withdrawal is successful, otherwise False.
        """
        try:
            # Fetch current balance
            
            values = (account_id,)
            self.db.cursor.execute(WITHDRAW_AMT_Q, values)
            current_balance = self.db.cursor.fetchone()

            if not current_balance:
                
                app_logger.log('error', f"Account ID {account_id} not found during withdrawal attempt.")
                print("Account not found.")
                return False
            
            current_balance = Decimal(current_balance[0])

            if current_balance - Decimal(amount) < self.__limit:
                app_logger.log('warning', f'Withdrawal failed for account id {account_id} due to minimal balance')
                print(f"Insufficient funds. Minimum balance of Rs.{self.__limit:.2f} must be maintained.")
                return False

            new_balance = current_balance - Decimal(amount)

            if not self.update_balance(self.account_id, new_balance):
                app_logger.log('error', f"Failed to update balance for account ID {account_id} after withdrawal of Rs{amount}")
                return False

            # Log the transaction
            self.transaction_manager.add_transaction(account_id=account_id, amount=amount, 
                                                     balance_after=new_balance, 
                                                     transaction_type="withdraw", 
                                                     description="Amount withdrawn from savings account")

            print(f"Withdrawal successful! New balance: Rs.{new_balance:.2f}")
            return True
        except mysql.connector.Error as err:
            print(f"Error during withdrawal: {err}")
            self.db.connection.rollback()
            return False
