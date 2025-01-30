def mydecorator(func):
    def wrapper(*args, **kwargs):
        return func (*args, **kwargs)
    return wrapper

@mydecorator
def greet(name):
    print(f"Hello {name}!")

greet("Alice")
greet("Bob")