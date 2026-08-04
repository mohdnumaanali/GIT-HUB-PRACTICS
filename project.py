import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
# Replace 'library_data.csv' with the actual filename of your CSV
df = pd.read_csv("library_data.csv")

# Step 2: Check the first few rows to confirm data loaded correctly
print(df.head())

# Step 3: Count Borrowed vs Submitted transactions
transaction_counts = df['Transaction'].value_counts()

# Step 4: Plot a bar graph
plt.figure(figsize=(6,4))
transaction_counts.plot(kind='bar', color=['steelblue','orange'])
plt.title("Library Transactions (Borrowed vs Submitted)")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
