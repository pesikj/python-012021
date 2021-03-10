# Streamovací služba podruhé

Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají. Vytvoř třídu `Uzivatel`, která bude mít atributy `uzivatelske_jmeno` a `delka_sledovani`, který udává celkovou délku pořadů, které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.

Třídám `Serial` a `Film` přidej funkce `get_celkova_delka()`, která vrátí celkovou délku filmu/seriálu (u seriálu je to počet episod násobený délkou jedné episody).

Třídě `Uzivatel` přidej funkci `pripocti_zhlednuti()`, která bude mít jeden parametr. Funkce zvýší atribut udávající celkovou délku sledávní o zadaný parametr.

Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování, využij k tomu funkci `get_celkova_delka()` u objektu a seriálu, abys zjistil(a), kolik minut (nebo hodin) videa celkem uživatel zhlédl.

Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a tuto pomocnou proměnnou potom předáš jako parametr funkci `pripocti_zhlednuti()`.

## Složitější varianta

V pokročilejší variantě neeviduj pouze délku sledování ale i to, jaké pořady uživatel sledoval. Namísto délky sledování vytvoř atribut, který bude udávat zhlédnuté pořady (ideální pro tento účel je seznam). Dále přidej funkci `zhledni_polozku()`, která do seznamu zhlédnutých pořadů přidánovou položku.

Dále vytvoř funkci `delka_sledování()` pro uživatele, která projde položky v seznamu a vrátí celkovou délku všech pořadů, které uživatel zhlédl.

Vytvoř si ukázkové objekty a ověř, že vše funguje.
