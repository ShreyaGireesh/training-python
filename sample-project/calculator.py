def add(a,b):
    """
    Adds two numbers and returns a value.
    """
    return a+b

def subtract(a,b):
    """
    Subtracts two numbers and returns a value.
    """
    return a-b

def multiply(a,b):
    """
    Multiply two numbers and returns a value.
    """
    return a*b

def divide(a,b):
    """
    Divides two numbers and returns a value.
    If second number is not given then by default it will take one.
    Division by zero is not possible.
    """
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator(operation, a, b=0):
    """
    Performs the operation on the provided two numbers.
    """
    if operation == 'add':
        return add(a, b)
    elif operation == 'subtract':
        return subtract(a, b)
    elif operation == 'multiply':
        return multiply(a, b)
    elif operation == 'divide':
        return divide(a, b)
    else:
        return "Invalid operation. Please choose from 'add', 'subtract', 'multiply', 'divide'."


print(calculator('add', 5, 3))        
print(calculator('subtract', 10, 4))  
print(calculator('multiply', 4, 2)) 