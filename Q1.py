import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

result_add = arr1+arr2
result_multiply = arr1*arr2
mean_result = np.mean(result_add)
max_value = np.max(result_multiply)

print("The sum of 2 arrays: ",result_add)
print("The product of 2 arrays: ",result_multiply)
print("The mean of array addition: ",mean_result)
print("The max value of array multiplication: ",max_value)
