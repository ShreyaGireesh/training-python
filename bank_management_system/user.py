from db_connection import Database
from constants import USER_CREATION
import mysql.connector

class UserManager:
    def __init__(self, db):
        self.db = db

    def create_user(self, name, phone_no,address=None):
        try:
            self.db.connection.start_transaction()
            values = (name, address, phone_no)
            self.db.cursor.execute(USER_CREATION, values)
            self.db.connection.commit() 
            user_id = self.db.cursor.lastrowid
            return user_id

        except mysql.connector.Error as err:
            print(f"Error while creating user: {err}")
            self.db.connection.rollback() 
            return None 

    def get_user(self, phone_no):
        try:
            self.db.connection.start_transaction()
            query = "SELECT user_id FROM users WHERE phone_no = %s"
            values = (phone_no,)
            self.db.cursor.execute(query, values)
            result = self.db.cursor.fetchone()
            if result:
                return result[0]  
            else:
                return None  
        except mysql.connector.Error as err:
            print(f"Error while fetching user: {err}")
            return None