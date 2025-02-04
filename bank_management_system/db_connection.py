import mysql.connector
from configparser import ConfigParser
from constants import DB_CONFIG_FILE

class Database:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.load_config()
        self.connect()

    def load_config(self):
        config = ConfigParser()
        config.read(DB_CONFIG_FILE)
        self.host = config.get('database', 'host')
        self.user = config.get('database', 'user')
        self.password = config.get('database', 'password')
        self.database = config.get('database', 'db')  
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            raise
            
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
