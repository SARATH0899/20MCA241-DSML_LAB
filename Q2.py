import numpy as np

grades = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])

result_mean = np.mean(grades)
result_average = np.average(result_mean)

print("Average of mean: ",result_average)

mask = grades > 90
result_grade_90 = np.sum(mask)
print("Number of students scored above 90: ", result_grade_90)

std_deviation = np.std(grades)
print("Standard Deviation: ",std_deviation)