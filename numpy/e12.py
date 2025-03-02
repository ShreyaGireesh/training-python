import numpy as np

arr = np.ones((3,3))

print(arr)

border_arr = np.pad(arr, pad_width = 1, mode = 'constant', constant_values =0 )

print(border_arr)