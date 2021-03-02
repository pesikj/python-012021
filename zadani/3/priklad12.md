# Půjčení auta

Pokračuj ve své práci pro autopůjčovnu, kterou jsi začala v [příkladu 11](priklad11.md).

Třídě `Auto` přidej funkci `pujc_auto()`, která nebude mít (kromě obligátního `self`) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, vrátí text `"Potvrzuji zapůjčení vozidla"` a změní hodnotu atributu, který určuje, zda je vozidlo půjčené. Pokud je vozidlo již půjčené, vrátí text `"Vozidlo není k dispozici"`.

Dále tříde `Auto` přidej funkci `get_info()`, která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty `Peugeot` nebo `Škoda`. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce `get_info()` a následně použij funkci `pujc_auto`.

Dotaz na uživatele a výpis výsledků si v programu zkopíruj, abys dokázala otestovat, že funkce nedovolí půjčit stejné auto dvakrát.
