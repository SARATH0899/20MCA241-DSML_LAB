import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Employee_Salary.csv')
plt.hist(df['Salary'], bins=10, edgecolor='black')

# Add quartiles to the plot
quartiles = df['Salary'].quantile([0.25, 0.50, 0.75])
plt.axvline(quartiles[0.25], color='r', linestyle='--', label='Q1')
plt.axvline(quartiles[0.50], color='y', linestyle='--', label='Q2 (Median)')
plt.axvline(quartiles[0.75], color='g', linestyle='--', label='Q3')

plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Salaries')

plt.legend()
plt.show()
