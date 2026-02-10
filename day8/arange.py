import numpy as np

# Using arange(Start, Stop, Step)
arr = np.arange(40,55,3)
print("Array of numbers:", arr)

print(arr.shape)
arr_1 = np.arange(1,17).reshape(4,4)
print(arr_1)

arr = np.linspace(0,2,5)
print(arr)

arr = np.random.rand(2,2)
print(arr)