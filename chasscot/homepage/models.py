from django.db import models

import datetime

# Create your models here.
class Produit(models.Model):
    nom_bouteille = models.CharField(max_length=40, default='')
    description_bouteille = models.CharField(max_length=500, default='')
    millésime = models.IntegerField(default=datetime.date.today().year)
    saison = models.CharField(max_length=20, default='')
    quantité = models.FloatField(default=0.5)
    pourcentage_alcool = models.FloatField(default=16)
    photo = models.ImageField(upload_to='uploads/', default='')
    prix = models.FloatField(default=10)
    pourcentage_rabais = models.FloatField(default=0)
    prix_final = models.FloatField(default=10)

class Membre(models.Model):
    nom = models.CharField(max_length=20)
    prénom = models.CharField(max_length=20)
    surnom = models.CharField(max_length=20)
    biographie = models.CharField(max_length=500)
    titre = models.CharField(max_length=20)
    photo_nain = models.ImageField(upload_to='uploads/', default='')
    photo_humain = models.ImageField(upload_to='uploads/', default='')

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prénom = models.CharField(max_length=100)
    nom_rue = models.CharField(max_length=250)
    numéro_de_rue = models.CharField(max_length=4)
    code_postal = models.CharField(max_length=4) #Ne pas oublier de forcer le int
    date_naissance = models.DateField()

class Etiquette(models.Model):
    modele_etiquette = models.ImageField(upload_to='uploads/', default='')

class Achat(models.Model):
    heure_achat_complet = models.DateTimeField(default=datetime.date.today())
    jour_achat = models.DateTimeField(default=datetime.date.today().day)
    mois_achat = models.DateTimeField(default=datetime.date.today().month)
    année_achat = models.DateTimeField(default=datetime.date.today().year)

class Client_B2B(models.Model):
    nom_contact = models.CharField(max_length=100)
    prénom_contact = models.CharField(max_length=100)
    nom_rue = models.CharField(max_length=250)
    numéro_de_rue = models.CharField(max_length=4)
    code_postal = models.CharField(max_length=4)  # Ne pas oublier de forcer le int
    date_naissance = models.DateField()
    nom_établissement = models.CharField(max_length=100)
    logo_établissement = models.ImageField(upload_to='uploads/', default='')
    type_établissement = models.CharField(max_length=100)
    url_site = models.URLField(max_length=300)