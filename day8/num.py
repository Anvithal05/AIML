import numpy as np

#Mean
data = np.array([[10,20,30],[40,50,60]])

print(np.mean(data))
print(np.mean(data, axis=0))

#median
data = np.array([10, 20, 30, 40, 50])

median_value = np.median(data)

print("Median:", median_value)

#Standard Deviation
data = np.array([10, 20, 30, 40, 50])

std_value = np.std(data)

print("Standard Deviation:", std_value)

#Matrix Multiplication
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))

#Transpose
A = np.array([[1, 2, 3],[4, 5, 6]])
transpose_A = A.T
print(transpose_A)

  
