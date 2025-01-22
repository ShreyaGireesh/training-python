def add(a,b):
    """
    Adds two numbers and returns a value.
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a+b

def subtract(a,b):
    """
    Subtracts two numbers and returns a value.
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The difference between the two numbers.
    """
    return a-b

def multiply(a,b):
    """
    Multiply two numbers and returns a value.
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The product of the two numbers.
    """
    return a*b

def divide(a,b):
    """
    Divides the first number by the second and returns the result.

    Parameters:
    a (int or float): The numerator.
    b (int or float): The denominator.

    Returns:
    float: The quotient of the two numbers.
    str: "Error! Division by zero." if the denominator is zero.
    
    Notes:
    If the second number is not provided, it defaults to 1.
    """
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator(operation, a, b=0):
    """
    Performs the operation on the provided two numbers.
    Parameters:
    operation (str): The operation to perform. Can be one of 'add', 'subtract', 'multiply', 'divide'.
    a (int or float): The first number.
    b (int or float, optional): The second number (default is 0).

    Returns:
    int, float, or str: The result of the operation, or an error message if the operation is invalid.

    For divide if second number is not provided default value is set to 1
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