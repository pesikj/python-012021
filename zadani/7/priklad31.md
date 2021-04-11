# Řazení

Vrať se k práci se souborem [temperature.csv](temperature.csv), který obsahuje informace o průměrné teplotě v různých městech v **listopadu 2017**.

```python
import wget
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
```

*Pokud jsi v předminulé lekci zpracovala rozšířené zadání, můžeš pracovat s teplotami ve stupních Celsia.*

* Vyfiltruj si informace o teplotách 13. listopadu 2017.
* Vyřaď všechny záznamy, které mají teplotu -99, protože tato hodnota je pravděpodobně chybná.
* Seřad hodnoty v souboru podle teploty od největší po nejmenší.
* Vypiš pět měst s nejvyšší teplotou a pět měst s nejnižší teplotou.
