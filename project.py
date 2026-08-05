import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("library_data.csv")

# Example dataset preview
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
plt.ylabel("")  # remove y-label
plt.show()

# 3️⃣ Line Chart (example: transactions over time if you have a Date column)
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])
    daily_counts = df.groupby(df['Date'].dt.date)['Transaction'].count()
    plt.figure(figsize=(8,4))
    daily_counts.plot(kind='line', marker='o')
    plt.title("Transactions Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Transactions")
    plt.grid(True)
    plt.show()

# 4️⃣ Histogram (example: distribution of student IDs if numeric)
if df['Student_ID'].dtype != 'object':
    plt.figure(figsize=(6,4))
    df['Student_ID'].plot(kind='hist', bins=20, color='purple', edgecolor='black')
    plt.title("Distribution of Student IDs")
    plt.xlabel("Student ID")
    plt.ylabel("Frequency")
    plt.show()

# 5️⃣ Scatter Plot (example: Student_ID vs Transaction index)
plt.figure(figsize=(6,4))
plt.scatter(df.index, df['Student_ID'], alpha=0.6, color='green')
plt.title("Scatter Plot of Student IDs")
plt.xlabel("Transaction Index")
plt.ylabel("Student ID")
plt.show()

# 6️⃣ Area Plot (cumulative transactions over time)
if 'Date' in df.columns:
    cumulative_counts = df.groupby(df['Date'].dt.date)['Transaction'].count().cumsum()
    plt.figure(figsize=(8,4))
    cumulative_counts.plot(kind='area', alpha=0.4, color='skyblue')
    plt.title("Cumulative Transactions Over Time")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Transactions")
    plt.show()

# 7️⃣ Stacked Bar Chart (example: Borrowed vs Submitted per day)
if 'Date' in df.columns:
    stacked_data = df.groupby([df['Date'].dt.date, 'Transaction']).size().unstack(fill_value=0)
    stacked_data.plot(kind='bar', stacked=True, figsize=(10,5))
    plt.title("Daily Transactions (Stacked)")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.show()

# 8️⃣ Box Plot (example: distribution of Student_IDs)
if df['Student_ID'].dtype != 'object':
    plt.figure(figsize=(6,4))
    df['Student_ID'].plot(kind='box')
    plt.title("Box Plot of Student IDs")
    plt.show()
