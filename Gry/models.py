from django.db import models

# Create your models here.
class Producent(models.Model):
 nazwa = models.CharField(max_length=40)
 opis = models.TextField(blank=True)

 def __str__(self):
  return self.nazwa

 class Meta:
  verbose_name = "Producent"
  verbose_name_plural = "Producenci"


class Kategoria(models.Model):
 nazwa = models.CharField(max_length=40)

 def __str__(self):
  return self.nazwa

 class Meta:
  verbose_name = "Kategoria"
  verbose_name_plural = "Kategorie"


class Gry(models.Model):
 kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True, blank=False)
 producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True, blank=False)
 nazwa = models.CharField(max_length=40)
 opis = models.TextField(blank=True)
 cena = models.DecimalField(max_digits=12, decimal_places=2)

 def __str__(self):
  return self.nazwa

 class Meta:
  verbose_name = "Gra"
  verbose_name_plural = "Gry"
