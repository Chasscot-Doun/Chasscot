from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Importation des bases de données
from .models import Produit

# Create your views here.
def index(request):
    liste_bouteilles = Produit.objects.all()

    context = {
        'bouteilles_en_vente': liste_bouteilles,
    }
    return render(request, 'homepage/index.html', context)
