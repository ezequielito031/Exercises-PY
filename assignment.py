import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


def get_crypto_data():
    return pd.DataFrame({
        "Day": [1, 2, 3, 4, 5, 6, 7],
        "Bitcoin": [40000, 42000, 41000, 45000, 44000, 46000, 48000],
        "Ethereum": [2500, 2600, 2550, 2800, 2750, 2900, 3100]
    })


def task_1_trend_line():
    df = get_crypto_data()
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df["Day"], df["Bitcoin"], marker='o', linestyle='--', color='navy', markersize=5, linewidth=1.5)
    ax.set_title("Bitcoin Price Over 7 Days")
    ax.set_xlabel("Day")
    ax.set_ylabel("Price ($)")
    ax.grid(True, linestyle='-', linewidth=0.5, alpha=0.7)
    plt.tight_layout()
    plt.savefig("task1_trend_line.png", dpi=150)
    plt.close()


def task_2_seaborn_comparison():
    data = pd.DataFrame({
        "Portfolio": ["Portfolio A", "Portfolio B", "Portfolio C"],
        "Total Value": [10000, 15000, 8000]
    })
    plt.figure(figsize=(7, 5))
    sns.barplot(data=data, x="Portfolio", y="Total Value")
    plt.title("Portfolio Value Comparison")
    plt.tight_layout()
    plt.savefig("task2_seaborn_comparison.png", dpi=150)
    plt.close()


def calculate_profit(buy_price, sell_price, quantity):
    return (sell_price - buy_price) * quantity


def calculate_roi(buy_price, sell_price):
    return ((sell_price - buy_price) / buy_price) * 100


def portfolio_total(holdings: dict):
    return sum(holdings.values())


if __name__ == "__main__":
    task_1_trend_line()
    task_2_seaborn_comparison()
