def fibonacci(n):
    """
    A generator that yields the first 'n' Fibonacci numbers.

    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Yields:
    int: A Fibonacci number in the sequence.
    
    """
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


fib_gen = fibonacci(10)

for number in fib_gen:
    print(number)
