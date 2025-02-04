
from db_connection import Database
from constants import ACCOUNT_CREATION
import mysql.connector
from decimal import Decimal
from transactions import TransactionManager


class AccountManager():
    def __init__(self, db):
        self.db = db
        self.transaction_manager = TransactionManager(db)
    

    def generate_accountno(self):
        self.db.cursor.execute("SELECT MAX(account_id) FROM accounts")
        max_account_id = self.db.cursor.fetchone()[0]
        new_account_id = max_account_id + 1 if max_account_id is not None else 1
        return f"ACC{new_account_id:07d}"

    def create_account(self, user_id, account_type, pin):
        try:
            self.db.connection.start_transaction()
            account_number = self.generate_accountno()
            values=(account_number, user_id, pin, account_type)
            self.db.cursor.execute(ACCOUNT_CREATION, values)
            self.db.connection.commit()
            self.display_account_details(account_number)
        except mysql.connector.Error as err:
            print(f"Error while creating user: {err}")
            self.db.connection.rollback()
            return None 
    
    def display_account_details(self, account_number):
        """Fetch account details from the database and display them in a creative format."""
        try:
            # Fetch account details from the database
            self.db.cursor.execute(
                "SELECT a.account_number, a.account_type, a.balance, u.user_id, u.user_name, u.phone_no "
                "FROM accounts a "
                "JOIN users u ON a.user_id = u.user_id "
                "WHERE a.account_number = %s", 
                (account_number,)
            )
            account_details = self.db.cursor.fetchone()

            if account_details:
                account_number, account_type, balance, user_id, name, phone_no = account_details

                # Print the account details in a creative format
                print("\n" + "*" * 50)
                print(f"** Account Details **")
                print("*" * 50)
                print(f"Account Number: {account_number}")
                print(f"Account Type: {account_type}")
                print(f"Balance: {Decimal(balance):,.2f}")
                print(f"User Name: {name}")
                print(f"User Email: {phone_no}")
                print("*" * 50)
            else:
                print("Error: Account not found!")

        except mysql.connector.Error as err:
            print(f"Error while fetching account details: {err}")

    def get_balance(self, account_number, pin):
        try:
            query = "SELECT balance FROM accounts WHERE account_number = %s AND pin = %s"
            values = (account_number, pin)
            self.db.cursor.execute(query, values)
            result = self.db.cursor.fetchone()

            if result:
                balance = result[0]
                return f"Your balance is: Rs.{balance:.2f}"
            else:
                return "Invalid account number or PIN."

        except mysql.connector.Error as err:
            print(f"Error while fetching balance: {err}")
            return None

    def get_account(self, account_number, pin):
        try:
            query = "SELECT account_id, account_type, balance FROM accounts WHERE account_number = %s and pin=%s"
            values = (account_number, pin)
            self.db.cursor.execute(query, values)
            result = self.db.cursor.fetchone()
            if result:
                account_id, account_type, balance = result
                return {"account_id": account_id, "account_type": account_type, "balance": balance}  # returning account_id and account_type
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error while fetching balance: {err}")
            return None

    def deposit_amount(self, account_id, amount):
        try:
            query = "SELECT balance FROM accounts WHERE account_id = %s"
            values = (account_id,)
            self.db.cursor.execute(query, values)
            current_balance = self.db.cursor.fetchone()

            new_balance = current_balance[0] + Decimal(amount)
            self.db.cursor.execute("UPDATE accounts SET balance = %s WHERE account_id =%s",(new_balance, account_id))
            self.db.connection.commit() 
            self.transaction_manager.add_transaction(account_id=account_id, amount=amount,balance_after=new_balance, transaction_type="deposit", description="Amount deposited")
            print("Amount successfully deposited")
        except mysql.connector.Error as err:
            print(f"Error while creating user: {err}")
            self.db.connection.rollback()
            return None 
        finally:
            self.db.close()

    def update_balance(self, account_id, balance):
        try:
            query = "UPDATE accounts SET balance = %s WHERE account_id = %s"
            values = (balance, account_id)
            self.db.cursor.execute(query, values)
            self.db.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error updating balance: {err}")
            self.db.connection.rollback()
            return False
        return True


class CurrentAccount(AccountManager):
    def __init__(self, db, account_id, balance, user_id):
        super().__init__(db)
        self.account_id = account_id
        self.balance = balance
        self.user_id = user_id
        self.account_type = "current"

    def withdraw_amount(self,account_id, amount):
        try:
            query = "SELECT balance FROM accounts WHERE account_id = %s"
            values = (account_id,)
            self.db.cursor.execute(query, values)
            current_balance = self.db.cursor.fetchone()

            if not current_balance:
                print("Account not found")
                return False

            current_balance = Decimal(current_balance[0])
            # if amount > current_balance:
            #     print("Insufficient balance.")
            #     return False
            new_balance = current_balance - Decimal(amount)

            if not self.update_balance(self.account_id, new_balance):
                return False

            self.transaction_manager.add_transaction(account_id=account_id, amount=amount, 
                                                     balance_after=new_balance, 
                                                     transaction_type="withdraw", 
                                                     description="Amount withdrawn from current account")
            
            print(f"Withdrawal successful! New balance: Rs.{new_balance:.2f}")
            return True
        except mysql.connector.Error as err:
            print(f"Error during withdrawal: {err}")
            self.db.connection.rollback()
            return False

class SavingsAccount(AccountManager):
    def __init__(self, db, account_id, balance, user_id):
        super().__init__(db)
        self.account_id = account_id
        self.balance = balance
        self.user_id = user_id
        self.account_type = "savings"
        self.__limit = Decimal(100)
    
    def withdraw_amount(self, account_id, amount):
        """Perform withdrawal for savings accounts (check minimum balance)."""
        try:
            # Fetch current balance
            query = "SELECT balance FROM accounts WHERE account_id = %s"
            values = (account_id,)
            self.db.cursor.execute(query, values)
            current_balance = self.db.cursor.fetchone()

            if not current_balance:
                print("Account not found.")
                return False
            
            current_balance = Decimal(current_balance[0])

            if current_balance - Decimal(amount) < self.__limit:
                print(f"Insufficient funds. Minimum balance of Rs.{self.__limit:.2f} must be maintained.")
                return False

            new_balance = current_balance - Decimal(amount)

            if not self.update_balance(self.account_id, new_balance):
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
