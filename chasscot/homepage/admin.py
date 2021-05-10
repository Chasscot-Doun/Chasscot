from django.contrib import admin
from .models import Produit, Membre, Utilisateur, Etiquette, Achat, Client_B2B

# Register your models here.
admin.site.register(Produit)
admin.site.register(Membre)
admin.site.register(Utilisateur)
admin.site.register(Etiquette)
admin.site.register(Achat)
admin.site.register(Client_B2B)