from db_connection import Database
from constants import USER_CREATION_Q
import mysql.connector
from datetime import datetime
from log_service import app_logger

class UserManager:
    def __init__(self, db):
        self.__db = db
        self.__name = None
        self.__phone_no = None
        self.__address = None
        self.__email = None
        self.__dob = None
        self.__gender = None

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_phone_no(self):
        return self.__phone_no
    
    def set_phone_no(self, phone_no):
        self.__phone_no = phone_no
    
    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address

    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email        

    def get_dob(self):
        return self.__dob
    
    def set_dob(self, dob):
        try:
            # Converting string dob (MM-DD-YYYY) into a MySQL DATE format (YYYY-MM-DD)
            dob = datetime.strptime(dob, "%m-%d-%Y").date() if dob else None
            self.__dob = dob
        except ValueError:
            app_logger.log('warning', 'Invalid date format entered')
            raise ValueError("Date must be in MM-DD-YYYY format")

    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        self.__gender = gender

    def create_user(self, name, phone_no,address=None, email=None, dob=None, gender=None):
        try:
            self.set_name(name)
            self.set_address(address)
            self.set_phone_no(phone_no)
            self.set_email(email)
            self.set_dob(dob)  # Ensure dob is converted to date format before saving
            self.set_gender(gender)

            self.__db.connection.start_transaction()
            app_logger.log('debug', f"Creating user with values: Name={name}, Phone={phone_no}, Address={address}, Email={email}, DOB={dob_converted}, Gender={gender}")
            values = (name, address, phone_no, email, self.get_dob(), gender)
            self.__db.cursor.execute(USER_CREATION_Q, values)
            
            self.__db.connection.commit() 
            user_id = self.db.cursor.lastrowid
            app_logger.log('info', f"User created with ID: {user_id}")
            return user_id

        except mysql.connector.Error as err:
            app_logger.log('error', f"Error while creating user: {err}")
            print(f"Error while creating user: {err}")
            self.db.connection.rollback() 
            return None 
