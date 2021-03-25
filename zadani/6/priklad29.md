# Teplota ve městech potřetí

Vrať se k práci se souborem [temperature.csv](temperature.csv), který obsahuje informace o průměrné teplotě v různých městech v **listopadu 2017**.

```python
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
```

*Pokud jsi v minulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.*

* Vyfiltruj si informace o teplotách 13. listopadu 2017.
* Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
* Vypočti počet dat, které máš pro daný den za jednotlivé regiony.
* Vypočti průměrnou teplotu za jednotlivé regiony.
* Vypočti maximální a minimální teplotu v každém regionu. 
