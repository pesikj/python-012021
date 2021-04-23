# Odkazy

Zkus své stránky propojit odkazy. K vytvoření odkazu použij tag `url`, který je opět [popsaný v dokumentaci](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#url). Níže máš příklad vytvoření odkazu na stránku, která je v souboru `url.py` (u aplikace, nikoli u projektu) pojmenovaná jako `index`.

```html
{% url 'index' %}
```
