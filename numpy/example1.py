import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr)
print(arr.dtype)  
print(arr.shape)
print(arr[1:5])
print(arr[4:])
print(arr[1:5:2])

print(np.zeros((3, 3)) )
arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr1)
print(arr1.shape)
print('2nd element on 1st row: ', arr1[0, 1])
print(arr1[1, 1:4])
print(arr1[0:2, 1:4])

arr2 = np.array([1, 2, 3, 4], dtype='i4')

print(arr2)
print(arr2.dtype)

arr3 = np.array([1, 0, 3])

newarr = arr3.astype(bool)

print(newarr)
print(newarr.dtype)