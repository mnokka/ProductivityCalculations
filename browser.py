import pandas as pd

money = pd.read_excel("money.xlsx", sheet_name="Sheet 1",header=9) # rivit 0-9 pois , rivi 10 alkaen
money = money.loc[:, ~money.columns.str.contains('Unnamed')] # remove "unnanamed" after the year 

workers = pd.read_excel("workers.xlsx", sheet_name="Sheet 1", header=9)
workers = workers.loc[:, ~workers.columns.str.contains('Unnamed')] 


def delimiter():
    print("-" * 40)


def print_data(df, name):
    print(name.upper())
    for year in ["2018", "2019"]:
        print(df[["TIME", year]])
        delimiter()



wanted_countries = ["Belgium", "Bulgaria", "Czechia", "Denmark", "Germany","Finland"]
subset_money = money[money["TIME"].isin(wanted_countries)]
subset_workers = workers[workers["TIME"].isin(wanted_countries)]

print_data(subset_money, "MONEYS")
print_data(subset_workers, "WORKERS")
