# Přidání výpůjčky

Vytvoř formulář na přidání výpůjčky, který umožní zákazníkům objednávat si výpůjčky automobilu.

### Rozšířené zadání

Uvažuj, že výpůjčky zadané do systému zákazníkem musí být nejprve schváleny. Přidej modelu `Vypujcka` pole, které bude evidovat, zda byla výpůjčka schválena (můžeš využít pole typu `BooleanField`). Jako výchozí hodnotu (`default`) nastav `False`. Dále přidej pohled a šablonu pro formulář, který bude sloužit k zadávání výpůjčky zákazníkem. Jako poslední uprav šablonu na výpis všech výpůjček tak, aby u neschválených výpůjček byla poznámka o tom, že nejsou schválené. K tomu využij tag `{% if %}`.
