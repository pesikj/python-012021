# Auto

Do souboru `models.py` přidej model `Auto`. U automobilů budeme evidovat následující údaje:

- registrační značka automobilu,
- značka a typ vozidla,
- počet najetých kilometrů,
- datum poslední technické kontroly.

Vyber pro každý údaj vhodný typ pole a název. Vystačíš si pouze s typy, které jsme používali na lekci, případně pro datum poslední kontroly můžeš zvolit typ `DateField` namísto `DateTimeField`.

Vytvoř nové soubory pro migraci, tj. spusť příkaz:

```
python manage.py makemigrations katalog
```

Následně proveď migraci příkazem:

```
python manage.py migrate
```
