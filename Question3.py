import pandas as pd

# Replace 'your_file_path.csv' with the path to your CSV file
python_file = 'titanic.csv'

# Read the CSV file
df = pd.read_csv(python_file)

# Step 1: Remove the 'deck' column
df_without_deck = df.drop(columns=['deck'])

# Step 2: Drop rows with any empty cells from the remaining columns
df_cleaned = df_without_deck.dropna()

# Calculate the number of observations lost
original_length = 891  # Original number of observations
new_length = len(df_cleaned)  # New length after cleaning
lost_observations = original_length - new_length

print(f"Number of lost observations after cleaning: {lost_observations}")
