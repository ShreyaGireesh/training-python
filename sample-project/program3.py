def planets(*names, sep='/'):
    return sep.join(names)

def custom_function(a,b,c):
    print(a,b,c)

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

print(planets('mercury', 'venus', 'earth'))
print(planets('mercury', 'venus', 'earth','mars', sep='.'))

num = 1,2,3
custom_function(*num)
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", 
    Age=25, Phone=9876543210)