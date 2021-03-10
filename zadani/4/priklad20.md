# Fake news

Moduly v Pythonu se často snaží zpříjemnit život programátorům. Například je občas otrava vymýšlet jména nebo adresy, když chceme vyzkoušet, jestli náš program funguje. Jindy třeba potřebujeme nějaká data anonymizovat, tj. odebrat z nich citlivé osobní údaje jako jména, adresy atd. Pro tento účel existuje modul `Faker`, která nám umí vygenerovat jména, adresy a řadu dalších dat, které můžeme využít při testování našich programů.

Nainstaluj si modul `Faker` pomocí postupu, který jsme si ukazovali na cvičení a je popsán v [příkladu 19](priklad19.md).

Níže máš příklad použití modulu. Nejprve provedeme import modulu, následně vytvoříme objekt `generator_falesnych_dat` třídy `Faker`. Využijeme parametr `"cs_CZ"`, který řekne modulu, aby nám generoval česká jména a adresy. Objekt `generator_falesnych_dat` má naprogramované funkce jako `name()` pro vygenerování náhodného jména, `address` pro vygenerování náhodné adresy atd.

```python

from faker import Faker
generator_falesnych_dat = Faker("cs_CZ")

print(generator_falesnych_dat.name())
print(generator_falesnych_dat.address())

```

Pojďme si modul vyzkoušet. Níže je třída `Balik`, která se podobá třídě, která už jsme vytvářeli během lekce. Náš balík má příjemce a adresu.

```python

class Balik:
  def get_info(self):
    print(f"Příjemce balíku: {self.name}")
    print(f"Balík doručte na adresu: {self.address}")

  def __init__(self, name, address):
    self.name = name
    self.address = address

```

Zkus nyní vytvořit nějaký objekt ze třídy `Balik` a přiřadit mu náhodně vygenerované jméno příjemce a adresu. Pomocí funkce `get_info()` si nech informace o balíku vypsat.

## Pokročilejší varianta

Uvažujme nyní společnost, která přepravuje balíky do více zemí. V [dokumentaci](https://faker.readthedocs.io/en/master/index.html) si najdi odstavec Localization. Tam najdeš informaci, že "`faker.Faker` also supports multiple locales". Podívej se, jak je v příkladu vytvořen objekt `Faker` (je použit seznam). Zkus nyní upravit svůj program tak, aby generoval adresy v rámci České i Slovenské republiky. Příslušnou zkratku pro Slovensko najdeš taktéž v [dokumentaci k modulu](https://faker.readthedocs.io/en/master/locales.html).
