# Další tagy

Zkus text doplnit o další HTML tagy. Příklad vidíš níže.

```python
return HttpResponse("""<h1>Vítejte v naší autopůjčovně!</h1>
<a href='http://localhost:8000/katalog/seznam/'>Jaká auta máme?</a><br>
<h2>O naší autopůjčovně</h2>
<p>Naše půjčovna vznikla v roce 2011 a dnes nabízí přibližně 30 aut.</p>
""")
```

Máme zde následující tagy:
- `h1` a `h2` pro nadpis první a druhé úrovně.
- `p` pro odstavec.
- `a` pro odkaz.
- `<br>` pro zalomení řádku. Tento tag není párový, tj. nemá uzavírací značku. Někdy se používá zápis `<br/>`, což je otevírací a uzavírací značka zároveň, ale prohlížeč obojí pochopí stejně.

Přidej do svého pohledu podobný text s využitím těchto tagů a podívej se, jak stránka vypadá v prohlížeči.

Pokud by sis chtěla vyzkoušet další tagy, můžeš například zkusit nečíslovaný seznam:

```
<ul>
  <li>Coffee</li>
  <li>Tea</li>
  <li>Milk</li>
</ul>
```
