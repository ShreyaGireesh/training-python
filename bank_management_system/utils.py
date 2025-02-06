import re
from datetime import datetime

class Validators:
    def __init__(self):
        self.phone_pattern = r'^\d{10}$'
        self.pin_pattern = r'\d{4}$'
        self.dob_pattern = r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-\d{4}$'
        self.email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  
        self.gender_pattern = r'^[MF]$'
        
    def validate_phoneno(self, phone_no):
        if re.match(self.phone_pattern, phone_no):
            return True
        return False

    def validate_pin(self, pin):
        if re.match(self.pin_pattern, pin):
            return True
        return False

    def validate_dob(self, dob):
        if re.match(self.dob_pattern, dob):
            try:
                datetime.strptime(dob, "%m-%d-%Y")
                return True
            except ValueError:
                
                return False
        return False
    
    def validate_email(self, email):
        """Validate email format"""
        return re.match(self.email_pattern, email)
    
    def validate_gender(self, gender):
        """Validate gender input ('M' or 'F')"""
        return re.match(self.gender_pattern, gender)