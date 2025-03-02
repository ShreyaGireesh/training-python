import numpy as np

arr_2d = np.random.randint(0, 10, (3,3))

arr_1d = np.random.randint(0, 10 , 3)

print(arr_2d)
print(arr_1d)

result = np.add(arr_2d, arr_1d)
print(result)