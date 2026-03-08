import pandas as pd

money = pd.read_excel("money.xlsx", sheet_name="Sheet 1",header=9) # rivit 0-9 pois , rivi 10 alkaen
workers = pd.read_excel("workers.xlsx")


def delimeter():
    print("-----------------------------------------------------------------------------")


#print(money.head(30))

df=money
#df = df.iloc[1:] # poista GEO rivi
#countries = df.iloc[18:22]
#print(countries)
#print(df.head(10))
#countries = df.iloc[7:] # line 18 Belgium

df = df.loc[:, ~df.columns.str.contains('Unnamed')] # remove unnanamed after the year 
subset = df.iloc[7:12] # Belgium-Germany

#print (countries)
#print(countries.head())

print("ALL MONEY DATA")
delimeter()
print(df.columns)
delimeter()
print(subset)
delimeter()

#print(df.iloc[7:12][["TIME", "2018"]])
#delimeter()
#delimeter()

#for i, row in df.iloc[7:12].iterrows():
#    print(row["TIME"], row["2018"])
#delimeter()

wanted_countries = ["Belgium", "Bulgaria", "Czechia", "Denmark", "Germany","Finland"]
subset = df[df["TIME"].isin(wanted_countries)]

print(subset[["TIME", "2018"]])
print(subset[["TIME", "2019"]])
