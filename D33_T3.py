# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Load dataset
df = pd.read_csv("Social_Network_Ads.csv")

# Features and target
X = df[['Age', 'EstimatedSalary']].values
y = df['Purchased'].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Function to plot decision boundary
def plot_decision_boundary(X, y, model, title):
    X1, X2 = np.meshgrid(
        np.arange(start=X[:, 0].min() - 1, stop=X[:, 0].max() + 1, step=0.01),
        np.arange(start=X[:, 1].min() - 1, stop=X[:, 1].max() + 1, step=0.01)
    )
    
    plt.contourf(X1, X2, model.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.title(title)
    plt.xlabel('Age (scaled)')
    plt.ylabel('Estimated Salary (scaled)')
    plt.show()

# K = 1 (Overfitting)
knn_1 = KNeighborsClassifier(n_neighbors=1)
knn_1.fit(X_train, y_train)
plot_decision_boundary(X_train, y_train, knn_1, "K = 1 (Very Complex Boundary)")

# K = 15 (Balanced)
knn_15 = KNeighborsClassifier(n_neighbors=15)
knn_15.fit(X_train, y_train)
plot_decision_boundary(X_train, y_train, knn_15, "K = 15 (Balanced Boundary)")

# K = 100 (Underfitting)
knn_100 = KNeighborsClassifier(n_neighbors=100)
knn_100.fit(X_train, y_train)
plot_decision_boundary(X_train, y_train, knn_100, "K = 100 (Very Smooth Boundary)")