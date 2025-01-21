num = [1,2,3,4,5]
squares = list(map(lambda x:x**2, num))
print(squares)
cubes = list(x**3 for x in num)
print(cubes)