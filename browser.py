import pandas as pd

money = pd.read_excel("money.xlsx", sheet_name="Sheet 1",header=9) # rivit 0-9 pois , rivi 10 alkaen
money = money.loc[:, ~money.columns.str.contains('Unnamed')] # remove unnanamed after the year 

workers = pd.read_excel("workers.xlsx", sheet_name="Sheet 1", header=9)
workers = workers.loc[:, ~workers.columns.str.contains('Unnamed')] 


def delimeter():
    print("-----------------------------------------------------------------------------")







wanted_countries = ["Belgium", "Bulgaria", "Czechia", "Denmark", "Germany","Finland"]
subset_money = money[money["TIME"].isin(wanted_countries)]

print("MONEYS")
print(subset_money[["TIME", "2018"]])
delimeter()
print(subset_money[["TIME", "2019"]])
delimeter()



subset_workers = workers[workers["TIME"].isin(wanted_countries)]

print ("WORKERS")
print(subset_workers[["TIME", "2018"]])
delimeter()
print(subset_workers[["TIME", "2019"]])
delimeter()
