# Simulating a user session
user_logged_in = True  

# The decorator for access control
def login_required(func):
    def wrapper():
        if user_logged_in:
            print("Access granted.")
            func()  
        else:
            print("Access denied. You need to log in.")
    return wrapper

# Applying the decorator to a function
@login_required
def view_profile():
    print("Displaying the user's profile.")

# Call the decorated function
view_profile()
