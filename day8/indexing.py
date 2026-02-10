import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row:', arr[0,1]) # arr[row, column]

#3D Indexing
arr = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
print(arr[0,1,2]) # arr[axis, row, column]

#1D Slicing
arr = np.array([1,2,3,4,5,6,7])
print(arr[1:5])