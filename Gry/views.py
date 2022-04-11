from django.shortcuts import render
from django.http import HttpResponse
from Gry.models import Gry, Kategoria


# Create your views here.


def index(request):
    # wszystkie = Gry.objects.all()
    # jeden = Gry.objects.get(pk=3)
    # kat = Gry.objects.filter(kategoria=1)
    # producent = Gry.objects.filter(producent=2)
    # null = Gry.objects.filter(kategoria__isnull=False)
    # zawiera = Gry.objects.filter(opis__icontains='f')
    # kat_nazwa = Kategoria.objects.get(id=5)
    kategorie = Kategoria.objects.all()
    dane = {'kategorie' : kategorie}
    return render(request, 'szablon.html', dane)


def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    return HttpResponse(kategoria_user.nazwa)

def gra(request, id):
    gra_user =Gry.objects.get(pk=id)
    text =  "<h1>" + str(gra_user) + "</h1>" + \
            "<p>" + str(gra_user.opis) + "</p>" + \
            "<p>" + str(gra_user.cena) + "</p>"
    return HttpResponse(text)