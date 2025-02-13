import time

# The decorator
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Applying the decorator to a function
@timer_decorator
def slow_function():
    time.sleep(3)  

# Call the decorated function
slow_function()