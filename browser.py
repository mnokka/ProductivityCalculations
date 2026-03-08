import pandas as pd
import os, sys
import matplotlib.pyplot as plt

# =================== EXCEL-TIEDOSTOT ===================
# money.xlsx sisältää tuotantoa rahassa (chain-linked volumes, index 2020=100)
# workers.xlsx sisältää työllisten määrät tuhansina henkilöinä
money_file = "money.xlsx"
workers_file = "workers.xlsx"

# =================== TIEDOSTOJEN TARKISTUS ===================
# Varmistetaan, että molemmat Excel-tiedostot löytyvät
for f in [money_file, workers_file]:
    if not os.path.exists(f):
        print(f"ERROR: Tiedostoa {f} ei löydy hakemistosta. Lopetetaan.")
        sys.exit(1)
print(f"OK: Kaikki tarvittavat Excel-tiedostot löytyvät {money_file},{workers_file}")

# =================== LUE EXCELIT ===================
# Poistetaan ylimääräiset rivit (header=9) ja sarakkeet, jotka Excelissä ovat "Unnamed"
money = pd.read_excel(money_file, sheet_name="Sheet 1", header=9)
money = money.loc[:, ~money.columns.str.contains('Unnamed')]

workers = pd.read_excel(workers_file, sheet_name="Sheet 1", header=9)
workers = workers.loc[:, ~workers.columns.str.contains('Unnamed')]

# =================== TUOTTAVUUSFUNKTIO ===================
def calc_productivity(money_df, workers_df, countries, years):
    """
    Laskee normalisoidun tuottavuuden halutuille maille ja vuosille.
    Tuottavuus per työntekijä lasketaan kaavalla:
        productivity = (normalisoitu raha / työlliset) * 1000
    Normalisointi tehdään suhteessa maksimiarvoon kullakin vuonna, jotta
    eri maiden absoluuttiset BKT-luvut eivät vääristä vertailua.
    """

    # Valitaan vain halutut maat
    subset_money = money_df[money_df["TIME"].isin(countries)]
    subset_workers = workers_df[workers_df["TIME"].isin(countries)]

    # =================== DEBUG ===================
    # Tarkistetaan, että Saksa löytyy oikein molemmista tiedostoista
    print("\n--- DEBUG: Germany in money.xlsx ---")
    print(subset_money[subset_money["TIME"]=="Germany"])
    print("\n--- DEBUG: Germany in workers.xlsx ---")
    print(subset_workers[subset_workers["TIME"]=="Germany"])

    # Kopioidaan rahasarakkeet productivity-taulukkoon
    productivity = subset_money[["TIME"] + years].copy()

    # =================== NORMALISOITU LASKENTA ===================
    for year in years:
        # Normalisointi: rahasarakkeen arvo / maksimi kyseisen vuoden rahasarakkeessa
        norm_money = subset_money[year] / subset_money[year].max()
        # Productivity = normalisoitu raha / työntekijät * 1000 (näkyvyyden vuoksi)
        productivity[year] = (norm_money / subset_workers[year]) * 1000

    return productivity

# =================== PARAMETRIT ===================
# Halutut maat ja vuodet analyysiin
wanted_countries = ["Belgium", "Bulgaria", "Czechia", "Denmark", "Germany", "Finland"]
wanted_years = ["2018", "2019", "2020", "2023"]

# =================== LASKENTA ========================
productivity = calc_productivity(money, workers, wanted_countries, wanted_years)

# =================== TULOSTUS ========================
print("\n----------------- PRODUCTIVITY (normalized) ---------------------------")
print(productivity)

# =================== PYLVÄSDIAGRAMMI ===================
# Visualisoidaan normalisoitu tuottavuus pylväsdiagrammina
df = productivity.set_index("TIME")  # asetetaan maat x-akselille

ax = df.plot(kind='bar', figsize=(10,6))
ax.set_ylabel("Relative Productivity (normalized)")
ax.set_title("Normalized Productivity by Country (2018, 2019, 2020, 2023)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =================== HUOMAUTUKSET LOPPUTYÖHÖN ===================
# - Normalisoitu tuottavuus kertoo suhteellisen tuottavuuden eri maiden välillä
# - Korkea pylväs = suhteellinen tuottavuus korkeampi; matala pylväs = pienempi
# - Absoluuttista rahallista tuottavuutta varten tarvitaan todellinen BKT euroina
# - Debug-osio voidaan poistaa lopullisesta versiossa