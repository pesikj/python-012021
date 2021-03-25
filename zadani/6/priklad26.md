# Zaměstnanci

```python

import wget

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

```

Uvažuj, že zpracováváš analýzu pro softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci. Seznam zaměstnanců pro jednotlivé kanceláře najdeš v souborech [zam_praha.csv](zam_praha.csv), [zam_plzeň.csv](zam_plzeň.csv) a [zam_liberec.csv](zam_liberec.csv).

* Načti data o zaměstnancích z CSV souborů do tabulek (`DataFrame`). Ke každé tabulce přidej nový sloupec `mesto`, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje. 
* Vytvoř novou tabulku `zamestnanci` a ulož do ní informace o všech zaměstnancích.
* Ze souboru [platy_2021_02.csv](platy_2021_02.csv) načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce `cislo_zamestnance`.
* Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
* Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.


## Dobrovolný doplněk

* Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
* V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují. Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.
