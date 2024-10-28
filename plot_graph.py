from itertools import count

import matplotlib.pyplot as plt
import pandas as pd

PPS_DATASET = "dataset/europe_purchasing_power_standard.csv"

df_data = pd.read_csv(PPS_DATASET)

years = []
countries = {}

for i, row in df_data.iterrows():
    year = row["Year"]
    country = row["Country"]
    pps_value = row["Purchasing_Power_Standard_B5N"]
    if year not in years:
        years.append(year)
    if country not in countries:
        countries[country] = []
        countries[country].append(pps_value)
    else:
        countries[country].append(pps_value)

fig, ax = plt.subplots(figsize=(6, 4), layout='constrained')

for country in countries:
    ax.plot(years, countries[country], label=country)

ax.legend()
ax.set_xlabel("Year")
# Purchasing Power Standard
ax.set_ylabel("PPS")
ax.set_title("Purchasing Power Standard\n Balance of Primary Incomes/National Income, Net")
plt.show()
