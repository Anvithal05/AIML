import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Set random seed for reproducibility
np.random.seed(42)

# 1️⃣ Generate datasets
normal_data = np.random.normal(loc=170, scale=10, size=1000)          # Human Heights (Normal)
right_skewed_data = np.random.exponential(scale=50000, size=1000)     # Household Income (Right-Skewed)
left_skewed_data = 100 - np.random.exponential(scale=10, size=1000)   # Easy Exam Scores (Left-Skewed)

# Convert to Pandas Series
normal_series = pd.Series(normal_data)
right_series = pd.Series(right_skewed_data)
left_series = pd.Series(left_skewed_data)

# 2️⃣ Plot Histograms with KDE
plt.figure(figsize=(18,5))

plt.subplot(1,3,1)
sns.histplot(normal_series, kde=True)
plt.title("Normal Distribution (Heights)")

plt.subplot(1,3,2)
sns.histplot(right_series, kde=True)
plt.title("Right-Skewed Distribution (Income)")

plt.subplot(1,3,3)
sns.histplot(left_series, kde=True)
plt.title("Left-Skewed Distribution (Easy Exam Scores)")

plt.tight_layout()
plt.show()

# 3️⃣ Compare Mean and Median
print("Normal Distribution:")
print("Mean:", normal_series.mean())
print("Median:", normal_series.median())
print()

print("Right-Skewed Distribution:")
print("Mean:", right_series.mean())
print("Median:", right_series.median())
print()

print("Left-Skewed Distribution:")
print("Mean:", left_series.mean())
print("Median:", left_series.median())
