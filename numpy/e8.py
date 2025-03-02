import numpy as np

# Normal Python function
def reverse_string(s):
    return s[::-1]

# Create a NumPy ufunc
reverse_ufunc = np.frompyfunc(reverse_string, 1, 1)

# Apply it to a NumPy array
arr = np.array(["Hello", "World", "Python"])
result = reverse_ufunc(arr)

print(result)  
