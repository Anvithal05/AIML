from sklearn.tree import DecisionTreeRegressor

# Training data
X = [[8,1],
     [8,3],
     [12,1],
     [12,4],
     [16,2]]   # Diameter, Toppings

y = [10,13,18,22.5,28]   # Price

# Create model
model = DecisionTreeRegressor()

# Train model
model.fit(X,y)

# Predict pizza price
price = model.predict([[14,2]])

print("Predicted Pizza Price:", price)