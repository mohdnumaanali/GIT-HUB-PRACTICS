import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("library_data.csv")

# ✅ Fix date parsing (DD-MM-YYYY format)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

print(df.head())

# Transaction counts
transaction_counts = df['Transaction'].value_counts()

# 1️⃣ Bar Chart
plt.figure(figsize=(6,4))
transaction_counts.plot(kind='bar', color=['steelblue','orange'])
plt.title("Library Transactions (Borrowed vs Submitted)")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 2️⃣ Pie Chart
plt.figure(figsize=(6,6))
transaction_counts.plot(kind='pie', autopct='%1.1f%%', colors=['steelblue','orange'])
plt.title("Library Transactions Distribution")
plt.ylabel("")
plt.show()

# 3️⃣ Line Chart (transactions over time)
daily_counts = df.groupby(df['Date'].dt.date)['Transaction'].count()
plt.figure(figsize=(8,4))
daily_counts.plot(kind='line', marker='o')
plt.title("Transactions Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Transactions")
plt.grid(True)
plt.show()
