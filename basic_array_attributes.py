import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr1d = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

shape = arr2d.shape
dimensions = arr2d.ndim
dtype = arr1.dtype

print(dtype)
print(shape)
print(dimensions)
