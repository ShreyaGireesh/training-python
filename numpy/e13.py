import numpy as np

def add_ten(x):
    return x + 10

ufunc_add_ten = np.frompyfunc(add_ten, 1, 1)

arr = np.array([1, 2, 3, 4, 5])

result = ufunc_add_ten(arr)

print(result)
