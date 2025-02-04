import re

class Validators:
    def __init__(self):
        self.phone_pattern = r'^\d{10}$'
        self.pin_pattern = r'\d{4}$'
        
    def validate_phoneno(phone_no):
        return re.match(phone_pattern, phone_no)

    def validate_pin(pin):
        return re.match(pin_pattern, pin)