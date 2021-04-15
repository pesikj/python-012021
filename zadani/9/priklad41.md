# Nastavení a migrace databáze

U tvého projektu ti doporučuji využít databázi SQLite, tj. neupravuj nastavení `DATABASES` v souboru `settings.py`. Důvodem je, že by se heslo k databázi dostalo do Gitu a koučové by měli složitější kontrolu příkladů, protože by museli konfiguraci změnit na nějakou svoji databázi.

Proveď tedy rovnou první migraci tvé aplikace:

```
python manage.py migrate
```

Dále přidej do seznamu `INSTALLED_APPS` tvoji aplikaci `katalog`, tj. do seznamu vlož hodnotu `katalog.apps.KatalogConfig`.
