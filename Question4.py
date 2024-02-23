import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file_path.csv' with the path to your CSV file
python_file = 'titanic.csv'

# Read the CSV file
df = pd.read_csv(python_file)

# Step 1: Calculate mean and standard deviation of 'fare'
mean_fare = df['fare'].mean()
std_fare = df['fare'].std()

# Step 2: Filter out observations with 'fare' outside the mean +/- 2*std range
lower_bound = mean_fare - 2 * std_fare
upper_bound = mean_fare + 2 * std_fare
filtered_df = df.loc[(df['fare'] >= lower_bound) & (df['fare'] <= upper_bound)]

# Step 3: Draw histograms and boxplots before and after removing extreme fares

# Before removing extremes
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df['fare'], density=True, bins=30, alpha=0.6, color='g')
plt.ylabel('Probability')
plt.xlabel('Fare')
plt.title('Histogram of Fare Before Filtering')

plt.subplot(1, 2, 2)
df.boxplot(column=['fare'])
plt.title('Boxplot of Fare Before Filtering')

plt.tight_layout()
plt.show()

# After removing extremes
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(filtered_df['fare'], density=True, bins=30, alpha=0.6, color='b')
plt.ylabel('Probability')
plt.xlabel('Fare')
plt.title('Histogram of Fare After Filtering')

plt.subplot(1, 2, 2)
filtered_df.boxplot(column=['fare'])
plt.title('Boxplot of Fare After Filtering')

plt.tight_layout()
plt.show()
