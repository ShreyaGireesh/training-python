import numpy as np

arr = np.zeros((5,5))

print(arr)

arr[0, :] = 1
arr[-1, :] = 1
arr[:, 0] = 1
arr[:, -1] = 1
print(arr)