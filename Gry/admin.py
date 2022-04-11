from django.contrib import admin
from .models import Gry, Producent, Kategoria, Wydawca

# Register your models here.
admin.site.register(Gry)
admin.site.register(Producent)
admin.site.register(Kategoria)
admin.site.register(Wydawca)
