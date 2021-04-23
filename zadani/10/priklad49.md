# Zákazníci

Jako poslední přidej přehled svých zákazníků. Opět vytvoř pohled a šablonu, přiřaď pohledu adresu a otestuj, že stránka funguje.

### Dobrovolný doplněk

Uvažuj, že půjčovna zavedla dva programy pro své pravidelné zákazníky: zlatý program a platinový program. Zákazníci, kteří nejsou členy ani jednoho programu, jsou označováni jako běžní zákazníci. Přidej k modelu `Zakaznik` nové pole, které bude určovat, zda si zákazník platí některý z programů. U pole omez dostupné možnosti na `běžný zákazník`, `zlatý program` a `platinový program`. K tomu použij parametr `choices`, jehož užití vidíš níže. 

Pro využití parametru `choices` si musíš vytvořit tzv. `tuple`, což je obdoba seznamu, pouze je zapsaný do kulatých závorek. Každá možnost má dvojici hodnot - jedna je zkratka (např. `S`) a druhá je hodnota zobrazovaná uživatelům (např. `Small`). Poli nastav parametr `null=True`, jako jsme to dělali např. u pole `kategorie` během lekce. Proveď migraci a ověř v administátorském rozhraní, že je nové pole k dispozici a je možná zadávat pouze jednu ze tří hodnot.

```python

from django.db import models

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```
