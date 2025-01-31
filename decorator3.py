def mydecorator(func):
    def wrapper(*args, **kwargs):
        if 'age' in kwargs:
            print(f"Age :{kwargs['age']}")
        if 'gender' in kwargs:
            print(f"Gender is {kwargs['gender']}")
        return func (*args, **kwargs)
    return wrapper

@mydecorator
def greet(name, **kwargs):
    print(f"Hello {name}!\n")

greet("Alice", age=25)
greet("Bob", age=30, gender='Female')
greet("John")