from db_connection import Database
from constants import USER_CREATION_Q
import mysql.connector
from datetime import datetime
from log_service import app_logger

class UserManager:
     """
    A class to manage user information and operations related to user creation.
    
    Attributes:
        __db (Database): The database connection object.
        __name (str): The user's name.
        __phone_no (str): The user's phone number.
        __address (str): The user's address.
        __email (str): The user's email.
        __dob (str): The user's date of birth.
        __gender (str): The user's gender.
    """
    def __init__(self, db):
        """
        Initializes the UserManager with a database connection.
        
        Args:
            db (Database): The database connection object to interact with the database.
        """
        self.__db = db
        self.__name = None
        self.__phone_no = None
        self.__address = None
        self.__email = None
        self.__dob = None
        self.__gender = None

    def get_name(self):
        """
        Retrieves the name of the user.
        
        Returns:
            str: The name of the user.
        """ 
        return self.__name
    
    def set_name(self, name):
        """
        Sets the name of the user.
        
        Args:
            name (str): The name of the user.
        """
        self.__name = name

    def get_phone_no(self):
        """
        Retrieves the phone number of the user.
        
        Returns:
            str: The phone number of the user.
        """
        return self.__phone_no
    
    def set_phone_no(self, phone_no):
        """
        Sets the phone number of the user.
        
        Args:
            phone_no (str): The phone number of the user.
        """
        self.__phone_no = phone_no
    
    def get_address(self):
        """
        Retrieves the address of the user.
        
        Returns:
            str: The address of the user.
        """
        return self.__address
    
    def set_address(self, address):
        """
        Sets the address of the user.
        
        Args:
            address (str): The address of the user.
        """
        self.__address = address

    def get_email(self):
        """
        Retrieves the email of the user.
        
        Returns:
            str: The email of the user.
        """
        return self.__email
    
    def set_email(self, email):
        """
        Sets the email of the user.
        
        Args:
            email (str): The email of the user.
        """
        self.__email = email        

    def get_dob(self):
        """
        Retrieves the date of birth of the user.
        
        Returns:
            datetime.date: The date of birth of the user.
        """
        return self.__dob
    
    def set_dob(self, dob):
        """
        Sets the date of birth of the user. Converts the string to a MySQL-compatible date format.
        
        Args:
            dob (str): The date of birth of the user in MM-DD-YYYY format.
        
        Raises:
            ValueError: If the date format is invalid.
        """
        try:
            
            dob = datetime.strptime(dob, "%m-%d-%Y").date() if dob else None
            self.__dob = dob
        except ValueError:
            app_logger.log('warning', 'Invalid date format entered')
            raise ValueError("Date must be in MM-DD-YYYY format")

    def get_gender(self):
        """
        Retrieves the gender of the user.
        
        Returns:
            str: The gender of the user.
        """
        return self.__gender
    
    def set_gender(self, gender):
        """
        Sets the gender of the user.
        
        Args:
            gender (str): The gender of the user.
        """
        self.__gender = gender

    def create_user(self, name, phone_no,address=None, email=None, dob=None, gender=None):
        """
        Creates a new user in the database with the provided details.
        
        Args:
            name (str): The name of the user.
            phone_no (str): The phone number of the user.
            address (str, optional): The address of the user. Defaults to None.
            email (str, optional): The email of the user. Defaults to None.
            dob (str, optional): The date of birth of the user in MM-DD-YYYY format. Defaults to None.
            gender (str, optional): The gender of the user. Defaults to None.
        
        Returns:
            int: The ID of the newly created user, or None if the operation failed.
        
        Raises:
            ValueError: If the date of birth is in an incorrect format.
        """
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
