# Přihlašování

Podívej se do manuálu na popis [LoginRequiredMixin](https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-loginrequired-mixin). Ten umožňuje omezit některý z pohledů pro nepřihlášené uživatele. Funguje to na základě dědičnosti: Tvůj pohled nebude dědit pouze od některé třídy typu `View`, ale též od třídy `LoginRequiredMixin`. Jednotlivé mateřské třídy oddělujeme čárkami a na pořadí záleží, třída `LoginRequiredMixin` by měla být jako první. Zkus nyní nastavit pro některý z pohledů, aby byly přístupné pouze pro přihlášené uživatele.

Protože zatím nemáš vytvořenou vlastní přihlašovací obrazovku, zkus využít tu pro administrátora. To uděláš tak, že nastavít atribut `login_url`, což je adresa, kam je uživatel přesměrován, aby se mohl přihlásit. Příklad vidíš níže.

```python
class ZakazniciView(LoginRequiredMixin, ListView):
    login_url = '/admin/login/'
    model = models.Zakaznik
    template_name = 'katalog/zakaznici_list.html'
```
