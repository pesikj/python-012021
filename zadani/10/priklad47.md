# Výpůjčky

Doplň svoji aplikaci o přehled výpůjček. Vytvoř pohled a šablonu přehled výpůjček, tj. záznamů modelu `Vypujcka`. Přiřaď pohledu URL adresu a zkontroluj, zda stránka funguje.

### Dobrovolný doplněk

Podívej se do [dokumentace](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#for-empty) na tag `for … empty`, který umožňuje zobrazit nějaký text, pokud v databázi nejsou uložené nějaké záznamy. Ošetři pomocí tagu situaci, že v databázi nejsou uloženy žádné výpůjčky.

Dále se podívej na [novou podkapitolu](https://kodim.cz/czechitas/progr2-python/zaklady-programovani-2/dedicnost/#vlastnosti-objektu) na webu [kodim.cz](https://kodim.cz/). Vlastnost (`property`) můžeš přidat i modelu v Djangu, níže je příklad celého jména jako vlastnost objektu. Zkus přidat novou vlastnost modelu `Vypujcka`, která bude poskytovat informaci o tom, jestli výpůjčka proběhla v minulosti, probíhá právě teď nebo je naplánovaná na budoucnost. Zobraz tuto vlastnost ve svém pohledu. Stačí přidat vlastnost od šablony úplně stejně, jako bys přidával(a) běžné pole.

```python
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
```
