import pandas as pd
import os, sys
import matplotlib.pyplot as plt

money_file = "money.xlsx"
workers_file = "workers.xlsx"

# =================== TIEDOSTOJEN TARKISTUS ===================
for f in [money_file, workers_file]:
    if not os.path.exists(f):
        print(f"ERROR: Tiedostoa {f} ei löydy hakemistosta. Lopetetaan.")
        sys.exit(1)
print(f"OK: Kaikki tarvittavat Excel-tiedostot löytyvät {money_file},{workers_file}")

# =================== LUE EXCELIT ===================
money = pd.read_excel(money_file, sheet_name="Sheet 1", header=9)  # rivi 0-9 pois
money = money.loc[:, ~money.columns.str.contains('Unnamed')]       # poista "Unnamed" sarakkeet

workers = pd.read_excel(workers_file, sheet_name="Sheet 1", header=9)
workers = workers.loc[:, ~workers.columns.str.contains('Unnamed')]

# =================== TUOTTAVUUSFUNKTIO ===================
def calc_productivity(money_df, workers_df, countries, years):
    # valitaan vain halutut maat
    subset_money = money_df[money_df["TIME"].isin(countries)]
    subset_workers = workers_df[workers_df["TIME"].isin(countries)]

    # =================== DEBUG: tarkista Saksa ===================
    print("\n--- DEBUG: Germany in money.xlsx ---")
    print(subset_money[subset_money["TIME"]=="Germany"])
    print("\n--- DEBUG: Germany in workers.xlsx ---")
    print(subset_workers[subset_workers["TIME"]=="Germany"])

    # Kopioidaan rahasarakkeet productivity-taulukkoon
    productivity = subset_money[["TIME"] + years].copy()

    # =================== NORMALISOITU LASKENTA ===================
    for year in years:
        # Normalisointi: rahasarakkeen arvo / maksimi kyseisen vuoden rahasarakkeessa
        # Tämä estää sen, että 2020 arvo 100000 kaikilla kaataa laskun
        norm_money = subset_money[year] / subset_money[year].max()
        # Productivity = normalisoitu raha / työntekijät, kerrotaan 1000 näkyvyyden vuoksi
        productivity[year] = (norm_money / subset_workers[year]) * 1000

    return productivity

# =================== PARAMETRIT ===================
wanted_countries = ["Belgium", "Bulgaria", "Czechia", "Denmark", "Germany","Finland"]
wanted_years = ["2018", "2019","2020","2023"]

# =================== LASKENTA ========================
productivity = calc_productivity(money, workers, wanted_countries, wanted_years)
print("\n----------------- PRODUCTIVITY (normalized) ---------------------------")
print(productivity)

# =================== PYLVÄSDIAGRAMMI ===================
df = productivity.set_index("TIME")  # maat x-akselille

ax = df.plot(kind='bar', figsize=(10,6))
ax.set_ylabel("Relative Productivity (normalized)")
ax.set_title("Normalized Productivity by Country (2018, 2019, 2020, 2023)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()