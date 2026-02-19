import numpy as np
import pandas as pd

# Set random seed
np.random.seed(42)

# Create sample dataset (Normal distribution + extreme outliers)
data = np.random.normal(loc=50, scale=10, size=1000)

# Add extreme values manually
data = np.append(data, [120, 130, -20])

# Create DataFrame
df = pd.DataFrame({"values": data})

# 1️⃣ Calculate Mean and Standard Deviation
mean = df["values"].mean()
std = df["values"].std()

print("Mean (μ):", mean)
print("Standard Deviation:", std)

# 2️⃣ Create Z-score column
df["z_score"] = (df["values"] - mean) / std

# 3️⃣ Identify outliers where |Z| > 3
outliers = df[np.abs(df["z_score"]) > 3]

print("\nOutliers (|Z| > 3):")
print(outliers)

print("\nTotal Outliers Found:", len(outliers))
