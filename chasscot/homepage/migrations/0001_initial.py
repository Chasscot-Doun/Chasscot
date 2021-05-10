# Generated by Django 3.2 on 2021-05-09 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure_achat_complet', models.DateTimeField(default=datetime.date(2021, 5, 9))),
                ('jour_achat', models.DateTimeField(default=9)),
                ('mois_achat', models.DateTimeField(default=5)),
                ('année_achat', models.DateTimeField(default=2021)),
            ],
        ),
        migrations.CreateModel(
            name='Client_B2B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contact', models.CharField(max_length=100)),
                ('prénom_contact', models.CharField(max_length=100)),
                ('nom_rue', models.CharField(max_length=250)),
                ('numéro_de_rue', models.CharField(max_length=4)),
                ('code_postal', models.CharField(max_length=4)),
                ('date_naissance', models.DateField()),
                ('nom_établissement', models.CharField(max_length=100)),
                ('logo_établissement', models.ImageField(default='', upload_to='uploads/')),
                ('type_établissement', models.CharField(max_length=100)),
                ('url_site', models.URLField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Etiquette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modele_etiquette', models.ImageField(default='', upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prénom', models.CharField(max_length=20)),
                ('surnom', models.CharField(max_length=20)),
                ('biographie', models.CharField(max_length=500)),
                ('titre', models.CharField(max_length=20)),
                ('photo_nain', models.ImageField(default='', upload_to='uploads/')),
                ('photo_humain', models.ImageField(default='', upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_bouteille', models.CharField(default='', max_length=40)),
                ('description_bouteille', models.CharField(default='', max_length=500)),
                ('millésime', models.IntegerField(default=2021)),
                ('saison', models.CharField(default='', max_length=20)),
                ('quantité', models.FloatField(default=0.5)),
                ('pourcentage_alcool', models.FloatField(default=16)),
                ('photo', models.ImageField(default='', upload_to='uploads/')),
                ('prix', models.FloatField(default=10)),
                ('pourcentage_rabais', models.FloatField(default=0)),
                ('prix_final', models.FloatField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prénom', models.CharField(max_length=100)),
                ('nom_rue', models.CharField(max_length=250)),
                ('numéro_de_rue', models.CharField(max_length=4)),
                ('code_postal', models.CharField(max_length=4)),
                ('date_naissance', models.DateField()),
            ],
        ),
    ]