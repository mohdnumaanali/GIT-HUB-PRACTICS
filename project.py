import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("library_data.csv")

print(df.head())

transaction_counts = df['Transaction'].value_counts()

plt.figure(figsize=(6,4))
transaction_counts.plot(kind='bar', color=['steelblue','orange'])
plt.title("Library Transactions (Borrowed vs Submitted)")
plt.xlabel("Transaction Type")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
