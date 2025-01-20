import random
from datetime import datetime, timedelta

import pandas as pd

CATEGORIES = [
    "Prepared Food", "Groceries",
    "Electronics", "Personal Care",
    "Entertainment & Social Activities",
    "Other"]

rows = []
for days_in_the_past in range(40):
    datetime = datetime.today() - timedelta(days=days_in_the_past)
    raw_date = datetime.strftime("%Y-%m-%d")
    rows.append([raw_date, random.choice(CATEGORIES),
                 random.randint(1, 10) + round(random.random(), 2)])
    while random.random() > 0.75:
        rows.append([raw_date, random.choice(CATEGORIES),
                     random.randint(1, 100) + round(random.random(), 2)])

rows.reverse()

csv_file_data = "Date,Category,Amount\n"
for row in rows:
    data = f"{row[0]},{row[1]},CA${row[2]}"
    csv_file_data = csv_file_data + data + "\n"

with open("data.csv", "w") as file:
    file.write(csv_file_data)
