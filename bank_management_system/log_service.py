import logging
from logging.handlers import RotatingFileHandler
import os
from configparser import ConfigParser

class LoggerService:
    """
    A class to handle logging functionality, including rotating logs to 
    a specified file with a maximum size and a defined number of backup files.
    """
    def __init__(self, log_file_path, log_level = logging.DEBUG):
         """
        Initializes the logger with the given log file path and log level.

        Args:
            log_file_path (str): The path to the log file.
            log_level (int, optional): The logging level to use. Defaults to logging.DEBUG.
        
        Raises:
            ValueError: If the log file path is not specified.
            Exception: For any unexpected error during logger initialization.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        try:
            if not log_file_path:
                raise ValueError("Log file path must be specified!")
            
            log_dir = os.path.dirname(log_file_path)
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            
            handler = RotatingFileHandler(log_file_path, maxBytes=10485760, backupCount=5)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
        
        except Exception as e:
            self.logger.error(f"Unexpected error during logger initialization: {e}")
            raise
        
    def log(self, level, message):
        """
        Logs a message at the specified log level.

        Args:
            level (str): The log level as a string ('info', 'warning', 'error', 'debug').
            message (str): The message to be logged.

        Raises:
            ValueError: If an invalid log level is provided.
        """
        if level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'debug':
            self.logger.debug(message)
        else:
            self.logger.error(f"Invalid log level: {level}")
    
def setup_logger():
    """
    Initializes the logger service by reading the configuration from a file.
    If the logger is already initialized, it returns the existing logger.

    Returns:
        LoggerService: The initialized LoggerService instance or None if initialization fails.
    
    Raises:
        Exception: If there is an error reading the configuration or initializing the logger.
    """
    global app_logger, logger_initialized
    if logger_initialized:
        
        return app_logger
    try:
        config = ConfigParser()  
        config.read('config.cfg')
        
        log_file_path = config.get("general", "log_file_path")
        log_level = config.get("general", "log_level", fallback="INFO").upper()
        
        app_logger = LoggerService(log_file_path=log_file_path, log_level=log_level)
        logger_initialized = True
        
        return app_logger
    except ValueError as ve:
        print(f"Logging Configuration Error: {ve}")
        print("Unable to initialize the logger due to invalid configuration.")
    except Exception as e:
        print(f"Unexpected Logging Error: {e}")
        print("An unexpected error occurred while initializing the logger.")

    return None

app_logger = None
logger_initialized = False
app_logger = setup_logger() 
