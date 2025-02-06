from db_connection import Database
from constants import USER_CREATION_Q
import mysql.connector
from datetime import datetime
from log_service import app_logger

class UserManager:
    def __init__(self, db):
        self.db = db

    def create_user(self, name, phone_no,address=None, email=None, dob=None, gender=None):
        try:
            if dob:
                dob_converted = datetime.strptime(dob, "%m-%d-%Y").strftime("%Y-%m-%d")
            self.db.connection.start_transaction()
            app_logger.log('debug', f"Creating user with values: Name={name}, Phone={phone_no}, Address={address}, Email={email}, DOB={dob_converted}, Gender={gender}")
            values = (name, address, phone_no, email, dob_converted, gender)
            self.db.cursor.execute(USER_CREATION_Q, values)
            self.db.connection.commit() 
            user_id = self.db.cursor.lastrowid
            app_logger.log('info', f"User created with ID: {user_id}")
            return user_id

        except mysql.connector.Error as err:
            app_logger.log('error', f"Error while creating user: {err}")
            print(f"Error while creating user: {err}")
            self.db.connection.rollback() 
            return None 
