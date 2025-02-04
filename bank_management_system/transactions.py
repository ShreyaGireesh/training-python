import mysql.connector
from decimal import Decimal

class TransactionManager:
    def __init__(self, db):
        self.db = db

    def add_transaction(self, account_id, transaction_type, amount, balance_after ,description, transaction_id_related=None):
        try:
            # Start transaction
            self.db.connection.start_transaction()

            # Insert transaction into the 'transactions' table
            query = """
                INSERT INTO transactions (from_account, transaction_type, amount, balance_after, description, transaction_id_related) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (account_id, transaction_type, Decimal(amount), balance_after ,description, transaction_id_related)
            self.db.cursor.execute(query, values)

            # Commit the transaction
            self.db.connection.commit()
            return True

        except mysql.connector.Error as err:
            print(f"Error while adding transaction: {err}")
            self.db.connection.rollback()
            return None
    
    def transaction_history(self, account_id):
        """Fetch and print transaction history for the given account."""
        try:
            # Fetch transaction history from the database
            query = """
                SELECT transaction_id, from_account, transaction_type, amount, transaction_date, balance_after, description
                FROM transactions
                WHERE from_account = %s
                ORDER BY transaction_date DESC
            """
            self.db.cursor.execute(query, (account_id,))
            transactions = self.db.cursor.fetchall()

            if transactions:
                print(f"\nTransaction History for Account {account_id}:\n")
                print(f"{'Transaction ID':<15}{'Type':<12}{'Amount':<10}{'Date':<25}{'Balance After':<15}{'Description'}")
                print("="*90)
                
                for transaction in transactions:
                    transaction_id, from_account, transaction_type, amount, transaction_date, balance_after, description = transaction
                    print(f"{transaction_id:<15}{transaction_type:<12}{amount:<10.2f}{transaction_date:<25}{balance_after:<15.2f}{description}")
            else:
                print(f"No transactions found for account {account_id}.")
        
        except mysql.connector.Error as err:
            print(f"Error while fetching transaction history: {err}")