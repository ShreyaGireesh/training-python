import mysql.connector
from configparser import ConfigParser
from constants import DB_CONFIG_FILE

class Database:
    """
    A class that handles the connection to a MySQL database. It loads 
    configuration from a specified file, connects to the database, 
    and provides methods to interact with the database.
    """
    def __init__(self):
        """
        Initializes the Database object by loading configuration settings
        and establishing a connection to the MySQL database.

        Raises:
            mysql.connector.Error: If there is an error connecting to the database.
        """
        self.connection = None
        self.cursor = None
        self.load_config()
        self.connect()

    def load_config(self):
        """
        Loads the database configuration (host, user, password, and database) 
        from the configuration file.

        Reads the `DB_CONFIG_FILE` to retrieve the database connection details.
        """
        config = ConfigParser()
        config.read(DB_CONFIG_FILE)
        self.host = config.get('database', 'host')
        self.user = config.get('database', 'user')
        self.password = config.get('database', 'password')
        self.database = config.get('database', 'db')  
    
    def connect(self):
        """
        Establishes a connection to the MySQL database using the loaded configuration.

        This method uses the MySQL Connector to connect to the database.
        
        Raises:
            mysql.connector.Error: If there is an error connecting to the MySQL database.
        """
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
        """
        Closes the database connection and cursor.

        This method ensures that both the cursor and connection are properly closed
        to release the resources after usage.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
