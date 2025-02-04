import logging
import time
import os
from logging.handlers import TimedRotatingFileHandler

# Set up the TimedRotatingFileHandler to rotate the log file every 10 seconds
log_file = 'shopping_cart.log'

# Create a TimedRotatingFileHandler: it will rotate the log every 10 seconds
handler = TimedRotatingFileHandler(log_file, when="s", interval=10, backupCount=3)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Set up the logger
logger = logging.getLogger()
logger.addHandler(handler)

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0
        logger.debug("ShoppingCart instance created. Initial state: empty cart.")
    
    def add_item(self, item, price):
        logger.debug(f"Adding item: {item} priced at ${price}. Current cart before adding: {self.items}")
        self.items.append(item)
        self.total_price += price
        logger.info(f"Item added: {item}. Current cart: {self.items}. Total price: ${self.total_price}")
    
    def remove_item(self, item, price):
        logger.debug(f"Trying to remove item: {item} priced at ${price}. Current cart before removal: {self.items}")
        if item in self.items:
            self.items.remove(item)
            self.total_price -= price
            logger.info(f"Item removed: {item}. Current cart: {self.items}. Total price: ${self.total_price}")
        else:
            logger.warning(f"Attempted to remove item not in cart: {item}")
    
    def checkout(self):
        logger.debug(f"Checkout attempt. Current cart: {self.items}, Total price: ${self.total_price}")
        if self.total_price > 1000:
            # Simulating an error for large cart total (e.g., payment gateway failure)
            logger.error(f"Checkout failed. Cart total ${self.total_price} exceeds the maximum limit of $1000.")
        elif self.items:
            logger.info(f"Checkout successful. Items: {self.items}. Total: ${self.total_price}")
            self.items.clear()
            self.total_price = 0
        else:
            logger.warning("Checkout attempted with empty cart.")
    
    def cause_critical_issue(self):
        # Simulating a critical issue, like a failure in payment processing
        try:
            raise Exception("Critical system failure during payment processing!")
        except Exception as e:
            logger.critical(f"Critical error: {e}")

# Simulate actions for just 10 seconds
cart = ShoppingCart()

start_time = time.time()  # Record the start time

# Keep logging for 10 seconds
while time.time() - start_time < 10:
    cart.add_item("Laptop", 800)
    cart.add_item("Phone", 300)  # This will cause the total to exceed $1000
    cart.checkout()
    time.sleep(1)  # Delay of 1 second between actions (to simulate actions over time)

# After 10 seconds, log rotation will automatically happen due to the handler
# You can check rotated logs, or manually stop logging after a time limit
# The log file will rotate every 10 seconds
