import numpy as np

arr = np.array([1, 2, 3, 4, 5])
copy_array = arr.copy()
arr[0] = 42

print(arr)
print(copy_array)

arr2 = np.array([1, 2, 3, 4, 5])
view_arr= arr2.view()
arr2[0] = 42

print(arr2)
print(view_arr)

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr3.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(6)
print(newarr)