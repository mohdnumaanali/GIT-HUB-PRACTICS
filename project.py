import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("library_data.csv")

df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

print(df.head())

transaction_counts = df['Transaction'].value_counts()

# Bar Chart
plt.figure(figsize=(6,4))
transaction_counts.plot(kind='bar', color=['steelblue','orange'])
plt.title("Library Transactions (Borrowed vs Submitted)")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
transaction_counts.plot(kind='pie', autopct='%1.1f%%', colors=['steelblue','orange'])
plt.title("Library Transactions Distribution")
plt.ylabel("")
plt.show()

# Line Chart (transactions over time)
daily_counts = df.groupby(df['Date'].dt.date)['Transaction'].count()
plt.figure(figsize=(8,4))
daily_counts.plot(kind='line', marker='o')
plt.title("Transactions Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Transactions")
plt.grid(True)
plt.show()

# Histogram (distribution of daily transactions)
plt.figure(figsize=(6,4))
daily_counts.plot(kind='hist', bins=10, color='purple', edgecolor='black')
plt.title("Histogram of Daily Transactions")
plt.xlabel("Number of Transactions")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot (index vs Transaction type)
plt.figure(figsize=(6,4))
plt.scatter(df.index, df['Transaction'].map({'Borrowed':1, 'Submitted':0}), alpha=0.6, color='green')
plt.title("Scatter Plot of Transactions")
plt.xlabel("Transaction Index")
plt.ylabel("Transaction (1=Borrowed, 0=Submitted)")
plt.show()

# Box Plot (distribution of daily transactions)
plt.figure(figsize=(6,4))
daily_counts.plot(kind='box')
plt.title("Box Plot of Daily Transactions")
plt.show()

# Stacked Bar Chart (Borrowed vs Submitted per day)
stacked_data = df.groupby([df['Date'].dt.date, 'Transaction']).size().unstack(fill_value=0)
stacked_data.plot(kind='bar', stacked=True, figsize=(10,5))
plt.title("Daily Transactions (Stacked)")
plt.xlabel("Date")
plt.ylabel("Count")
plt.show()

# Area Plot (cumulative transactions)
cumulative_counts = daily_counts.cumsum()
plt.figure(figsize=(8,4))
cumulative_counts.plot(kind='area', alpha=0.4, color='skyblue')
plt.title("Cumulative Transactions Over Time")
plt.xlabel("Date")
plt.ylabel("Cumulative Transactions")
plt.show()
