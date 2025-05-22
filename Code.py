import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Dataset
df = pd.read_csv("StudentsPerformance.csv")

# Step 2 & 3: Explore Data & Check for Missing Values
print(df.info())
print(df.describe())
print("Missing Values:\n", df.isnull().sum())

# Step 4: Analyze Score Patterns
print(df.groupby("gender")[["math score", "reading score", "writing score"]].mean())

# Step 5: Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar Plot - Average Math Score by Gender
sns.barplot(x="gender", y="math score", data=df, ax=axes[0])
axes[0].set_title("Average Math Score by Gender")

# Histogram - Distribution of Math Scores
sns.histplot(df["math score"], bins=20, kde=True, ax=axes[1])
axes[1].set_title("Distribution of Math Scores")

plt.tight_layout()
plt.show()
