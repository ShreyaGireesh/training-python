import mysql.connector
from decimal import Decimal
from datetime import datetime
from log_service import app_logger

class TransactionManager:
    """
    A class to manage transactions for user accounts.
    
    Attributes:
        __db (Database): The database connection object.
    """
    def __init__(self, db):
        """
        Initializes the TransactionManager with a database connection.
        
        Args:
            db (Database): The database connection object to interact with the database.
        """
        self.__db = db

    def add_transaction(self, account_id, transaction_type, amount, balance_after ,description, transaction_id_related=None):
         """
        Adds a new transaction to the 'transactions' table.
        
        Args:
            account_id (int): The ID of the account for the transaction.
            transaction_type (str): The type of transaction (e.g., 'Deposit', 'Withdrawal').
            amount (float): The transaction amount.
            balance_after (float): The account balance after the transaction.
            description (str): A description of the transaction.
            transaction_id_related (int, optional): The related transaction ID for this transaction (if any).
        
        Returns:
            bool: True if the transaction was added successfully, None if an error occurred.
        
        Raises:
            mysql.connector.Error: If there is an error while interacting with the database.
        """
        try:
            # Start transaction
            self.__db.connection.start_transaction()

            # Insert transaction into the 'transactions' table
            query = """
                INSERT INTO transactions (from_account, transaction_type, amount, balance_after, description, transaction_id_related) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (account_id, transaction_type, Decimal(amount), balance_after ,description, transaction_id_related)
            self.__db.cursor.execute(query, values)

            # Commit the transaction
            self.__db.connection.commit()
            app_logger.log('info', f"Transaction added: {transaction_type} of Rs {amount} for account {account_id}.")
            return True

        except mysql.connector.Error as err:
            print(f"Error while adding transaction: {err}")
            app_logger.log('error', f"Error while adding transaction for account {account_id}: {err}")
            self.__db.connection.rollback()
            return None
    
    def transaction_history(self, account_id, account_number):
        """
        Fetches and displays the transaction history for a given account.
        
        Args:
            account_id (int): The ID of the account for which the transaction history is being fetched.
            account_number (str): The account number associated with the transactions.
        
        Returns:
            None: Prints the transaction history to the console.
        
        Raises:
            mysql.connector.Error: If there is an error while interacting with the database.
        """
        try:
            # Fetch transaction history from the database
            query = """
                SELECT from_account, transaction_type, amount, transaction_date, balance_after, description, transaction_id_related
                FROM transactions
                WHERE from_account = %s OR transaction_id_related = %s
                ORDER BY transaction_date DESC
            """
            self.__db.cursor.execute(query, (account_id, account_id))
            transactions = self.__db.cursor.fetchall()
            
            if transactions:

                app_logger.log('info', f"Fetched transaction history for account {account_number}.")
                print(f"\n{'-'*40}Transaction History for Account {account_number}{'-'*40}\n")
                
                # Print headers in the specified order
                print(f"{'Date':<25}{'From Account':<15}{'Type':<12}{'Amount':<10}{'Balance After':<15}{'To Account':<20}{'Description'}")
                print("-" * 120)

                # Loop through the transactions and print each row
                for txn in transactions:
                    # Unpack the result of each row to match the 7 columns
                    from_account, txn_type, amount, txn_date, balance_after, description, txn_id_related = txn

                    # Format the transaction_date for better readability
                    if txn_date:
                        txn_date = txn_date.strftime('%Y-%m-%d %H:%M:%S')  # format it as 'YYYY-MM-DD HH:MM:SS'
                    else:
                        txn_date = "N/A"

                    # Handle None for the transaction_id_related column
                    txn_id_related = txn_id_related if txn_id_related is not None else "N/A"

                    # Print the formatted transaction details in the specified order
                    print(f"{txn_date:<25}{from_account:<15}{txn_type:<12}{amount:<10}{balance_after:<15}{txn_id_related:<20}{description}")
                
                print("-" * 120)
            else:
                app_logger.log('warning', f"No transactions found for account {account_number}")
                print(f"No transactions found for account {account_number}")

        
        except mysql.connector.Error as err:
            app_logger.log('error', f"Error while fetching transaction history for account {account_number}: {err}")
            print(f"Error while fetching transaction history: {err}")