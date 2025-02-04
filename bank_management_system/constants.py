DB_CONFIG_FILE = "config.cfg"
USER_ACCOUNT_SUCCESS = "Account created successfully!"


USER_CREATION = "INSERT INTO users (user_name, address, phone_no) VALUES (%s, %s, %s)"
ACCOUNT_CREATION = "INSERT INTO accounts(account_number, user_id, pin, account_type) VALUES(%s, %s, %s, %s)"