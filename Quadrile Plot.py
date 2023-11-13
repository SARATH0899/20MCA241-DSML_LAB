import seaborn as sns
import matplotlib.pyplot as plt

data = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

# Create a quartile plot (box plot) using Seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(y=data, color='yellow')
plt.title('Quartile Plot Example')
plt.ylabel('Value')
plt.show()
