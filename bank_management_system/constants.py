DB_CONFIG_FILE = "config.cfg"
USER_ACCOUNT_SUCCESS = "Account created successfully!"


USER_CREATION_Q = "INSERT INTO users (user_name, address, phone_no, email, dob, gender) VALUES (%s, %s, %s, %s, %s, %s)"
ACCOUNT_CREATION_Q = "INSERT INTO accounts(account_number, user_id, pin, account_type) VALUES(%s, %s, %s, %s)"
GET_BALANCE_Q = "SELECT balance FROM accounts WHERE account_number = %s AND pin = %s"
GET_ACCOUNT_Q = "SELECT account_id, account_type, balance FROM accounts WHERE account_number = %s and pin=%s"
DEPOSIT_AMOUNT_Q = "SELECT balance FROM accounts WHERE account_id = %s"
UPDATE_BALANCE_Q = "UPDATE accounts SET balance = %s WHERE account_id = %s"
WITHDRAW_AMT_Q = "SELECT balance FROM accounts WHERE account_id = %s"
ONLY_BALANCE_Q = "SELECT balance FROM accounts WHERE account_id=%s"
CHECK_ACC_EXISTS_Q = "SELECT account_id, account_type, balance FROM accounts WHERE account_number = %s"


INVALID_ACC_DETAILS_MSG = "Account creation failed due to invalid details"
ACC_NOT_FOUND = "Error: Account not found!"
SUCCESS_AMT_DEPOSIT = "Amount successfully deposited"