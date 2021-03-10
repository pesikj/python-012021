# Streamovací služba

Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa. Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry. Dále chce u filmů evidovat délku a u seriálů počet episod a délku jedné episody.

- Vytvoř program, který bude obsahovat tři třídy - `Polozka`, `Film` a `Serial`.
- Třída `Polozka` bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr. Oba atributy nastav ve funkci `__init__()`, žánr získej jako parametr funkce.
- Třída `Film` bude potomkem třídy `Polozka`. Film má kromě názvu a žánru atribut délka.
- Třída `Serial` bude potomkem třídy `Polozka`. Má kromě názvu a žánru atributy počet epizod a délka epizody.
- Všem třídám přidej funkci `get_info()`, která vypíše informace o položce, resp. o filmu a seriálu. Funkce u třídy `Polozka` vypíše název a žánr. Následně tuto funkci využij ve funkcích u tříd `Film` a `Serial` a přidej k ní informaci o délce, resp. počtu episod.

Po naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál o ověr, že vše funguje.
