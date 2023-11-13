import pandas as pd

data = {'Name':['Alice','Bob','Charlie'],
        'Age':[25,30,35],
        'City':['New York','San Fransico','Los Angeles']}
df = pd.DataFrame(data)

print(df)

df1 = pd.read_csv('sample.csv')
print("\n")
print(df1)

df2 = pd.read_csv('sales_data.csv')
revenue_sum = df2['Revenue'].sum()
num_rows, num_columns = df2.shape
print("\n")
print("The Number of Row: ",num_rows)
print("The Number of column: ",num_columns)
print("The Total Revenue: ",revenue_sum)