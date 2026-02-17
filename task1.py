import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
data = {
    "Price": [200000, 220000, 250000, 275000, 300000, 320000,
              350000, 400000, 450000, 500000, 800000],
    "City": ["New York", "New York", "Chicago", "Chicago",
             "Los Angeles", "Los Angeles",
             "Chicago", "New York",
             "Los Angeles", "Chicago",
             "New York"]
}

df = pd.DataFrame(data)
plt.figure()
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of Housing Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print("Skewness:", skewness)
print("Kurtosis:", kurtosis)

plt.figure()
sns.countplot(x="City", data=df)
plt.title("Number of Houses per City")
plt.show()
