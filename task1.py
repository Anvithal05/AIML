import pandas as pd

# Create sample data
data = {
    "Transmission": ["Automatic", "Manual", "Automatic", "Manual", "Automatic"],
    "Color": ["Red", "Blue", "Green", "Blue", "Red"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df["Transmission"] = le.fit_transform(df["Transmission"])

print("\nAfter Label Encoding (Transmission):")
print(df)

df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nAfter One-Hot Encoding (Color):")
print(df)
