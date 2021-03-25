# Státy světa potřetí

```python

import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

```

V souboru [staty.json](staty.json) jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali. Zkusme nyní zpracovat podobné úlohy pomocí `pandas`.

* Načti data ze souboru do tabulky.
* Vyfiltruj státy, které leží v Evropě.
* Zjisti počet států v jednotlivých subregionech Evropy.
* Zjisti cekový počet obyvatel v jednotlivých subregionech Evropy.

## Rozšíření zadání

V souboru [staty.json](staty.json) jsou uložena data s informacemi o státech světa, se kterými jsme již pracovali. V souboru [gdp.csv](gdp.csv) jsou dále informace o hrubém domácím produktu (Gross Domestic Product - GDP) států za roky 2017-2019 ze Světové banky.

* Načti informace ze souborů do tabulek. Z tabulky s GDP odeber státy, které nemají kompletní informace GDP (tj. ponech pouze státy, které mají kompletní data za všechny tři roky).
* Propoj obě tabulky podle třípísmenného kódu států.
* Spočti celkové HDP za rok 2019 a celkový počet obyvatel za jednotlivé subregiony.
* Projdi si subkapitolu o [počítaných sloupcích](https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/#pocitane-sloupce) (část o podmínených sloupcích není nutné číst). K tabulce, kterou jsi vytovřila v předchozím kroku, vypočti GDP v roce 2019 na obyvatele, tj. přidej sloupec s velikostí GDP v roce 2019 vydělenou počtem obyvatel daného subregionu.
