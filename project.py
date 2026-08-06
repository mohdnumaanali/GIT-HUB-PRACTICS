# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("library_data.csv")

# df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# print(df.head())

# transaction_counts = df['Transaction'].value_counts()

# # Bar Chart
# plt.figure(figsize=(6,4))
# transaction_counts.plot(kind='bar', color=['steelblue','orange'])
# plt.title("Library Transactions (Borrowed vs Submitted)")
# plt.xlabel("Transaction Type")
# plt.ylabel("Number of Students")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()

# # Pie Chart
# plt.figure(figsize=(6,6))
# transaction_counts.plot(kind='pie', autopct='%1.1f%%', colors=['steelblue','orange'])
# plt.title("Library Transactions Distribution")
# plt.ylabel("")
# plt.show()

# # Line Chart (transactions over time)
# daily_counts = df.groupby(df['Date'].dt.date)['Transaction'].count()
# plt.figure(figsize=(8,4))
# daily_counts.plot(kind='line', marker='o')
# plt.title("Transactions Over Time")
# plt.xlabel("Date")
# plt.ylabel("Number of Transactions")
# plt.grid(True)
# plt.show()

# # Histogram (distribution of daily transactions)
# plt.figure(figsize=(6,4))
# daily_counts.plot(kind='hist', bins=10, color='purple', edgecolor='black')
# plt.title("Histogram of Daily Transactions")
# plt.xlabel("Number of Transactions")
# plt.ylabel("Frequency")
# plt.show()

# # Scatter Plot (index vs Transaction type)
# plt.figure(figsize=(6,4))
# plt.scatter(df.index, df['Transaction'].map({'Borrowed':1, 'Submitted':0}), alpha=0.6, color='green')
# plt.title("Scatter Plot of Transactions")
# plt.xlabel("Transaction Index")
# plt.ylabel("Transaction (1=Borrowed, 0=Submitted)")
# plt.show()

# # Box Plot (distribution of daily transactions)
# plt.figure(figsize=(6,4))
# daily_counts.plot(kind='box')
# plt.title("Box Plot of Daily Transactions")
# plt.show()

# # Stacked Bar Chart (Borrowed vs Submitted per day)
# stacked_data = df.groupby([df['Date'].dt.date, 'Transaction']).size().unstack(fill_value=0)
# stacked_data.plot(kind='bar', stacked=True, figsize=(10,5))
# plt.title("Daily Transactions (Stacked)")
# plt.xlabel("Date")
# plt.ylabel("Count")
# plt.show()

# # Area Plot (cumulative transactions)
# cumulative_counts = daily_counts.cumsum()
# plt.figure(figsize=(8,4))
# cumulative_counts.plot(kind='area', alpha=0.4, color='skyblue')
# plt.title("Cumulative Transactions Over Time")
# plt.xlabel("Date")
# plt.ylabel("Cumulative Transactions")
# plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='whitegrid')
TRANSACTION_ORDER = ['Borrowed', 'Submitted']
COLORS = ['#1f77b4', '#ff7f0e']


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    expected = {'Roll Number', 'Student Name', 'Transaction', 'Date', 'Book Title'}
    missing = expected - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}")

    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')
    df['Transaction'] = (
        df['Transaction']
        .astype(str)
        .str.strip()
        .str.capitalize()
        .replace({'Borrowed': 'Borrowed', 'Submitted': 'Submitted'})
    )

    df = df.dropna(subset=['Date', 'Transaction'])
    df = df[df['Transaction'].isin(TRANSACTION_ORDER)].copy()
    df = df.drop_duplicates()
    return df


def summarize_transactions(df: pd.DataFrame) -> pd.Series:
    return df['Transaction'].value_counts().reindex(TRANSACTION_ORDER, fill_value=0)


def get_daily_transaction_counts(df: pd.DataFrame) -> pd.Series:
    daily = df.groupby(df['Date'].dt.date)['Transaction'].count()
    daily.index = pd.to_datetime(daily.index)
    return daily.sort_index()


def get_transaction_pivot(df: pd.DataFrame) -> pd.DataFrame:
    pivot = df.pivot_table(
        index=df['Date'].dt.date,
        columns='Transaction',
        values='Roll Number',
        aggfunc='count',
        fill_value=0,
    )
    pivot.index = pd.to_datetime(pivot.index)
    return pivot.reindex(columns=TRANSACTION_ORDER, fill_value=0).sort_index()


def plot_transaction_distribution(counts: pd.Series) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    sns.barplot(x=counts.index, y=counts.values, palette=COLORS, ax=axes[0])
    axes[0].set_title('Borrowed vs Submitted')
    axes[0].set_xlabel('Transaction Type')
    axes[0].set_ylabel('Count')

    for i, value in enumerate(counts.values):
        axes[0].text(i, value + 0.3, str(value), ha='center')

    axes[1].pie(
        counts.values,
        labels=counts.index,
        autopct='%1.1f%%',
        colors=COLORS,
        startangle=140,
        wedgeprops={'edgecolor': 'white'},
    )
    axes[1].set_title('Transaction Distribution')
    axes[1].axis('equal')

    plt.tight_layout()
    plt.show()


def plot_transactions_over_time(daily_counts: pd.Series) -> None:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x=daily_counts.index, y=daily_counts.values, marker='o', color=COLORS[0], ax=ax)
    ax.set_title('Daily Transactions Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Transactions')
    ax.grid(True, alpha=0.4)
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()


def plot_daily_stats(daily_counts: pd.Series) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    sns.histplot(daily_counts, bins=8, color=COLORS[0], edgecolor='black', ax=axes[0])
    axes[0].set_title('Histogram of Daily Transactions')
    axes[0].set_xlabel('Transactions per Day')
    axes[0].set_ylabel('Frequency')

    sns.boxplot(x=daily_counts, color=COLORS[1], ax=axes[1])
    axes[1].set_title('Box Plot of Daily Transactions')
    axes[1].set_xlabel('Transactions per Day')

    plt.tight_layout()
    plt.show()


def plot_stacked_daily_transactions(pivot: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    pivot.plot(kind='bar', stacked=True, color=COLORS, ax=ax)
    ax.set_title('Daily Borrowed and Submitted Transactions')
    ax.set_xlabel('Date')
    ax.set_ylabel('Count')
    ax.legend(title='Transaction')
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()


def plot_cumulative_transactions(daily_counts: pd.Series) -> None:
    cumulative = daily_counts.cumsum()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(
        x=cumulative.index,
        y=cumulative.values,
        marker='o',
        color=COLORS[1],
        ax=ax,
    )
    ax.fill_between(cumulative.index, cumulative.values, alpha=0.2, color=COLORS[1])
    ax.set_title('Cumulative Transactions Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Cumulative Count')
    ax.grid(True, alpha=0.4)
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.show()


def print_summary(df: pd.DataFrame, counts: pd.Series, daily_counts: pd.Series) -> None:
    print('Total transactions:', len(df))
    print(counts.to_string())
    print('Date range:', daily_counts.index.min().date(), 'to', daily_counts.index.max().date())
    print('Days with transactions:', len(daily_counts))
    print('Average daily transactions:', round(daily_counts.mean(), 2))


def main() -> None:
    path = 'library_data.csv'
    df = load_data(path)
    counts = summarize_transactions(df)
    daily_counts = get_daily_transaction_counts(df)
    pivot = get_transaction_pivot(df)

    print_summary(df, counts, daily_counts)

    plot_transaction_distribution(counts)
    plot_transactions_over_time(daily_counts)
    plot_daily_stats(daily_counts)
    plot_stacked_daily_transactions(pivot)
    plot_cumulative_transactions(daily_counts)


if __name__ == '__main__':
    main()