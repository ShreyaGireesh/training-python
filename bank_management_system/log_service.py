import logging
from logging.handlers import RotatingFileHandler
import os
from configparser import ConfigParser

class LoggerService:
    def __init__(self, log_file_path, log_level = logging.DEBUG):
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
        """Log message at the specified level."""
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
    """Initializes the logger using the global config variable."""
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
