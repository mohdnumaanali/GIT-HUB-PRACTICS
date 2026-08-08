from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

df = pd.read_csv("library_data.csv")
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bar_chart.png")
def bar_chart():
    transaction_counts = df['Transaction'].value_counts()
    plt.figure(figsize=(6,4))
    transaction_counts.plot(kind='bar', color=['steelblue','orange'])
    plt.title("Library Transactions (Borrowed vs Submitted)")
    plt.xlabel("Transaction Type")
    plt.ylabel("Number of Students")
    plt.xticks(rotation=0)
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return send_file(buf, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
