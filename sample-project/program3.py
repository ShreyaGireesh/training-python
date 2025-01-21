def planets(*names, sep='/'):
    return sep.join(names)

def custom_function(a,b,c):
    print(a,b,c)

print(planets('mercury', 'venus', 'earth'))
print(planets('mercury', 'venus', 'earth','mars', sep='.'))

num = 1,2,3
custom_function(*num)
