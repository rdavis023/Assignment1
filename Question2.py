import pandas as pd

# Replace 'your_file_path.csv' with the path to your CSV file
python_file = 'titanic.csv'

# Read the CSV file
df = pd.read_csv(python_file)

# Original length of the DataFrame
original_length = len(df)

# Remove rows with any empty cells
df_cleaned = df.dropna()

# New length after removing rows with empty cells
new_length = len(df_cleaned)

# Calculate the number of removed observations/rows
removed_rows = original_length - new_length

print(f"Number of removed observations/rows: {removed_rows}")
