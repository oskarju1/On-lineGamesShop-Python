from django.shortcuts import render
from django.http import HttpResponse
from Gry.models import Gry, Kategoria, Producent


# Create your views here.


def index(request):
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    return render(request, 'template.html', dane)


def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_gra = Gry.objects.filter(kategoria=kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user,
            'kategoria_gra': kategoria_gra,
            'kategorie': kategorie}
    return render(request, 'kategoria_gra.html', dane)

def producent(request, id):
    producent_user = Producent.objects.get(pk=id)
    producent_gra = Gry.objects.filter(producent=producent_user)
    producenci = Producent.objects.all()
    dane = {'producent_user': producent_user,
            'producent_gra': producent_gra,
            'producenci': producenci}
    return render(request, 'producent_gra.html', dane)


def gra(request, id):
    gra_user = Gry.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'gra_user': gra_user, 'kategorie': kategorie}
    return render(request, 'gra.html', dane)
