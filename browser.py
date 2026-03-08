

import pandas as pd
import os,sys
import matplotlib.pyplot as plt

money_file = "money.xlsx"
workers_file = "workers.xlsx"

# Tarkistus molemmille tiedostoille
for f in [money_file, workers_file]:
    if not os.path.exists(f):
        print(f"ERROR: Tiedostoa {f} ei löydy hakemistosta. Lopetetaan.")
        sys.exit(1)
print(f"OK: Kaikki tarvittavat excel tiedostot löytyvät {money_file},{workers_file}")


# lue execlit pandas dataframeiksi
money = pd.read_excel(money_file, sheet_name="Sheet 1",header=9) # rivit 0-9 pois , rivi 10 alkaen
money = money.loc[:, ~money.columns.str.contains('Unnamed')] # # siivousta "unnamed" pois vuosien vierestä

workers = pd.read_excel(workers_file, sheet_name="Sheet 1", header=9)
workers = workers.loc[:, ~workers.columns.str.contains('Unnamed')] # siivousta "unnamed" pois vuosien vierestä



####################################################################################
def calc_productivity(money_df, workers_df, countries, years):
    subset_money = money_df[money_df["TIME"].isin(countries)]
    subset_workers = workers_df[workers_df["TIME"].isin(countries)]
    
    productivity = subset_money[["TIME"] + wanted_years].copy()
    print ("----------------- PRODUCTIVITY ---------------------------")
    for year in years:
        productivity[year] = subset_money[year] / subset_workers[year]
    
    return productivity

####################################################################################


wanted_countries = ["Belgium", "Bulgaria", "Czechia", "Denmark", "Germany","Finland"]
wanted_years = ["2018", "2019","2020","2023"]

#========================= LASKENTA ========================
productivity = calc_productivity(money, workers, wanted_countries, wanted_years)
print(productivity)


# =================== PYLVÄSDIAGRAMMI ===================
df = productivity.set_index("TIME")  # maat x-akselille

ax = df.plot(kind='bar', figsize=(10,6))
ax.set_ylabel("Productivity")
ax.set_title("Productivity by Country (2018, 2019, 2020, 2023)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()