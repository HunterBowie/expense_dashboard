from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data.csv")
data["Date"] = pd.to_datetime(data["Date"])
data['Date'] = data['Date'].dt.date
one_week_ago = datetime.today() - timedelta(weeks=1, days=1)
one_week_ago = one_week_ago.date()
data_filtered = data[data["Date"] > one_week_ago]
data_filtered = data_filtered[data_filtered["Date"] < datetime.today().date()]

print(data_filtered)

"""So, right now I have filtered the data so its just the past week of expenses"""


# plt.bar(data["Category"], data[])

# plt.show()
