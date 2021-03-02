# Rezervace

Vytvoř rezervační program pro rekreační středisko. Ve středisku jsou následující ceny za osobu a noc:

| Datum | Cena |
| ------------- |-------------:| 
| 1. 6. 2021 - 30. 6. 2021 | 600 Kč | 
| 1. 7. 2021 - 31. 8. 2021 | 900 Kč |

Mimo tato data je středisko zavřené.

Tvůj program se nejprve zeptá uživatele na datum příjezdu a počet osob, pro které uživatel chce ubytování rezervovat. Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce `datetime.strptime()`. Následně se zeptej  na počet osob, 

Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že středisko je v té době uzavřené. Pokud je středisko otevřené, spočítej a vypiš cenu za ubytování.

Data lze porovnávat pomocí známých operátorů `<`, `>`, `<=`, `>=`, `==`, `!=`. Tyto operátory můžeš použít v podmínce `if`. Níže vidíš příklad porovnání dvou datumů. Program vypíše text `"První datum je dřívější než druhé datum."`.

```python
from datetime import datetime
prvni_udalost = datetime(2021, 6, 1)
druha_udalost = datetime(2021, 6, 3)
if prvni_datum < druhe_datum:
  print("Druhá událost se stala po první události")
```
