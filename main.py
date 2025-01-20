from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd

from constants import CATEGORIES, COLORS

data = pd.read_csv("data.csv")
data["Amount"] = data["Amount"].apply(lambda amount: float(amount[3:]))
data["Date"] = pd.to_datetime(data["Date"])
data['Date'] = data['Date'].dt.date
one_week_ago = datetime.today() - timedelta(weeks=1, days=1)
one_week_ago = one_week_ago.date()
data_filtered = data[data["Date"] > one_week_ago]
data_filtered = data_filtered[data_filtered["Date"] < datetime.today().date()]

data_bar_graph = pd.DataFrame(columns=["Category", "Amount"])
for category in CATEGORIES:
    only_category = data_filtered[data_filtered["Category"] == category]
    data_bar_graph.loc[len(data_bar_graph)] = [
        category, only_category["Amount"].sum()]

print(data_bar_graph)

fig, ax = plt.subplots()
ax.bar(data_bar_graph["Category"], data_bar_graph["Amount"], color=COLORS)
ax.tick_params(axis="x", labelsize=8)
fig.set_size_inches(12, 8)

for i, value in enumerate(data_bar_graph["Amount"]):
    plt.text(i, value + 0.5,
             f"${round(value)}",
             ha='center',
             va='bottom',
             fontsize=10)
ax.set_ylabel("Amount ($)")
ax.set_title("Spending by Category (last week)")
fig.patch.set_facecolor('lightblue')
ax.set_facecolor('#dfdfdf')

plt.show()
