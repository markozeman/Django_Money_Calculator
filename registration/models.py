from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime



class Uporabnik(models.Model):
    uporabnik = models.OneToOneField(User, on_delete=models.CASCADE)
    # bancno_stanje = models.OneToOneField(Stanje, on_delete=models.CASCADE)
    # denarnica_stanje = models.OneToOneField(Stanje, on_delete=models.CASCADE)
    #cilji = models.ManyToOneRel("Cilj", on_delete=models.CASCADE)
    #transakcije = models.ManyToManyField(Transakcija, on_delete=models.CASCADE)

    def __str__(self):
        return self.uporabnik


class Stanje(models.Model):
    tip = models.CharField(max_length=20, default='')
    stanje = models.FloatField(default=0)
    uporabnik = models.ForeignKey(Uporabnik, on_delete=models.CASCADE, default='')

    #izdatki = models.ForeignKey(IzdatekPrejemek)
    #prejemki = models.ForeignKey(IzdatekPrejemek)

    def __str__(self):
        return self.tip


class IzdatekPrejemek(models.Model):
    tip = models.CharField(max_length=20, default='')
    opis = models.CharField(max_length=100, default='')
    znesek = models.FloatField()
    kategorija = models.CharField(max_length=30, default='')
    datum = models.DateTimeField(default=datetime.now)
    banka_denarnica = models.CharField(max_length=20, default='')
    stanje = models.ForeignKey(Stanje, on_delete=models.CASCADE)

    def __str__(self):
        return self.tip


class Transakcija(models.Model):
    opis = models.CharField(max_length=100, default='')
    znesek = models.FloatField()
    smer = models.CharField(max_length=20)
    uporabnik = models.ForeignKey(Uporabnik, on_delete=models.CASCADE)

    def __str__(self):
        return self.opis


class Cilj(models.Model):
    opis = models.CharField(max_length=150, default='')
    vrednost = models.FloatField()
    trenutno_privarcevano = models.FloatField(default=0)
    od_datuma = models.DateTimeField(default=datetime.now)
    do_datuma = models.DateTimeField()
    uporabnik = models.ForeignKey(Uporabnik, on_delete=models.CASCADE)

    def __str__(self):
        return self.opis




