# ProductivityCalculations
POC to calculate Countries manufacturing productivities / graphics using EU data (https://ec.europa.eu/eurostat)


Using EU Gross value and Employment files from:

https://ec.europa.eu/eurostat/databrowser/view/nama_10_a10__custom_20421522/default/table
https://ec.europa.eu/eurostat/databrowser/view/nama_10_a10_e/default/table?lang=en&category=na10.nama10.nama_10_e_p


*browser.py defines*

```
wanted_countries = ["Belgium", "Bulgaria", "Czechia", "Denmark", "Germany","Finland"]
wanted_years = ["2018", "2019","2020","2023"]
```

*brower.py produces* 

```
----------------- PRODUCTIVITY ---------------------------
        TIME      2018      2019      2020      2023
7    Belgium  0.021175   0.02139  0.020512  0.022035
8   Bulgaria  0.028311  0.029741  0.029359  0.033129
9    Czechia  0.018969  0.019681  0.019131  0.019848
10   Denmark   0.03401  0.034094   0.03366  0.034362
11   Germany  0.002313  0.002308  0.002224  0.002302
32   Finland  0.038588  0.038644   0.03861  0.037373
```


*Execute command*

```
python3 browser.py
```