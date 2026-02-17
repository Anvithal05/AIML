import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500],
    "Price": [200000, 250000, 300000, 360000, 400000, 450000, 480000, 550000],
    "Location": ["Urban", "Urban", "Suburban", "Suburban", "Suburban", "Urban", "Urban", "Suburban"]
}

df = pd.DataFrame(data)

# Scatter Plot
plt.figure()
plt.scatter(df["SquareFootage"], df["Price"])
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Square Footage vs Price")
plt.show()

plt.figure()
sns.boxplot(x="Location", y="Price", data=df)
plt.title("Location vs Price")
plt.show()
