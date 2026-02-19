import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
np.random.seed(42)

# 1️⃣ Create heavily right-skewed dataset (like income)
population = np.random.exponential(scale=50000, size=10000)

# Plot original skewed distribution
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.histplot(population, kde=True)
plt.title("Original Population (Right-Skewed Income)")

# 2️⃣ Take 1000 samples of size 30 and calculate means
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# 3️⃣ Plot distribution of sample means
plt.subplot(1,2,2)
sns.histplot(sample_means, kde=True)
plt.title("Distribution of 1000 Sample Means (n=30)")

plt.tight_layout()
plt.show()

# 4️⃣ Print comparison statistics
print("Original Population Mean:", np.mean(population))
print("Mean of Sample Means:", np.mean(sample_means))

print("\nOriginal Population Std Dev:", np.std(population))
print("Std Dev of Sample Means:", np.std(sample_means))
