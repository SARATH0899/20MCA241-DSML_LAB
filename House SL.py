from sklearn.linear_model import LinearRegression

# DataSet
No_of_Rooms = [3, 4, 2, 4, 3]
Sq_Feet = [1500, 1800, 1200, 2000, 1600]
Age_of_House = [10, 5, 20, 15, 8]
Price = [250000, 320000, 180000, 330000, 280000]

# Reshape the data for sklearn input
X = list(zip(No_of_Rooms, Sq_Feet, Age_of_House))
y = Price

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predicting the price for a house with given values
X1 = input("Enter the No.of Rooms: ")
X2 = input("Enter the Sq Feet: ")
X3 = input("Enter the Age: ")
new_data = list(zip(No_of_Rooms, Sq_Feet, Age_of_House))
predicted_price = model.predict(new_data)
print("Predicted price of the house:", predicted_price[0])