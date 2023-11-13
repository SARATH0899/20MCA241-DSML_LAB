import pandas as pd

data = {'Student_id':['S1A100','S1A102','S1A106','S1B103','S1B105','S2A108','S2B104','S3A101','S3B110','S3B109'],
        'Name':['Sarath','Shon','Siddharth','Sreerag','Sudeesh','Nithin','Sreehari','Subin','Philip','Sobin'],
        'Age':[24,22,23,20,19,18,22,18,21,19],
        'GPA':[88.7,85.3,79.5,91.7,74.0,80.9,83.5,86.0,90.5,84.8]}

df = pd.DataFrame(data)

num_row_age = df[df['Age'] >= 20]
print("Q1. The Number of students older than 20 years: \n",num_row_age)
print("\n")

gpa_avg = df['GPA'].mean()
print("Q2. The Average GPA of the students: ",gpa_avg)
print("\n")

des_ord = df.sort_values(by='GPA', ascending=False).head(5)
print("Q3. Sorted by GPA in Descending Order with highest 5 toppers: \n",des_ord)
print("\n")

age_gpa = df.groupby('Age')['GPA'].mean()
print("Q4. Sorted by Age & Average GPA of each age group : \n",age_gpa)

