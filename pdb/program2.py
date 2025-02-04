def divide(a, b):
    return a / b  # Potential ZeroDivisionError

def main():
    x = 10
    y = 0  # This will cause a division by zero error
    result = divide(x, y)
    print(result)

if __name__ == "__main__":
    main()