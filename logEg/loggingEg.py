import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename = 'shopping_cart.log',
                    filemode = 'a')

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0
        logging.debug("ShoppingCart instance created. Initial state: empty cart.")
    
    def add_item(self, item, price):
        logging.debug(f"Adding item: {item} priced at ${price}. Current cart before adding: {self.items}")
        self.items.append(item)
        self.total_price += price
        logging.info(f"Item added: {item}. Current cart: {self.items}. Total price: ${self.total_price}")
    
    def remove_item(self, item, price):
        logging.debug(f"Trying to remove item: {item} priced at ${price}. Current cart before removal: {self.items}")
        if item in self.items:
            self.items.remove(item)
            self.total_price -= price
            logging.info(f"Item removed: {item}. Current cart: {self.items}. Total price: ${self.total_price}")
        else:
            logging.warning(f"Attempted to remove item not in cart: {item}")
    
    def checkout(self):
        logging.debug(f"Checkout attempt. Current cart: {self.items}, Total price: ${self.total_price}")
        if self.total_price > 1000:
            # Simulating an error for large cart total (e.g., payment gateway failure)
            logging.error(f"Checkout failed. Cart total ${self.total_price} exceeds the maximum limit of $1000.")
        elif self.items:
            logging.info(f"Checkout successful. Items: {self.items}. Total: ${self.total_price}")
            self.items.clear()
            self.total_price = 0
        else:
            logging.warning("Checkout attempted with empty cart.")
    
    def cause_critical_issue(self):
        # Simulating a critical issue, like a failure in payment processing
        try:
            raise Exception("Critical system failure during payment processing!")
        except Exception as e:
            logging.critical(f"Critical error: {e}")

# Simulate actions
cart = ShoppingCart()

cart.add_item("Laptop", 800)

cart.add_item("Phone", 300)  # This will cause the total to exceed $1000

# cart.remove_item("Phone", 300)
cart.checkout()

# Simulate a critical error
cart.cause_critical_issue()
