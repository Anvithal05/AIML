# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Drop customerID (not useful)
df = df.drop("customerID", axis=1)

# Convert TotalCharges to numeric (some values are blank)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')

# Fill missing values
df = df.fillna(df["TotalCharges"].median())

# Convert target to binary
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

# One-Hot Encoding for categorical features
df = pd.get_dummies(df, drop_first=True)

# Split features and target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Euclidean Distance (p=2)
knn_euclidean = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
knn_euclidean.fit(X_train, y_train)

y_pred_euclidean = knn_euclidean.predict(X_test)
acc_euclidean = accuracy_score(y_test, y_pred_euclidean)

print("Accuracy (Euclidean):", acc_euclidean)

# Manhattan Distance (p=1)
knn_manhattan = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=1)
knn_manhattan.fit(X_train, y_train)

y_pred_manhattan = knn_manhattan.predict(X_test)
acc_manhattan = accuracy_score(y_test, y_pred_manhattan)

print("Accuracy (Manhattan):", acc_manhattan)