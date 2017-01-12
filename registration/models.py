from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group, Permission
from datetime import datetime, timedelta


class Stanje(models.Model):
    """ Class representing Stanje.

    This is Stanje model, each Uporabnik has two Stanjes.

    """
    tip = models.CharField(max_length=20, default='')
    stanje = models.FloatField(default=0)
    uporabnik = models.ForeignKey(User, on_delete=models.CASCADE, default='')


    def __str__(self):
        return ("{} - {}: {}".format(self.uporabnik.username, self.tip, self.stanje))

    def is_negative(self):
        """ Returns True if Stanje is negative

        Returns True if Stanje is negative, False otherwise.

        """
        return  self.stanje < 0


class IzdatekPrejemek(models.Model):
    """ Class representing IzdatekPrejemek.

    This is IzdatekPrejemek model, each Stanje can have more IzdatekPrejemeks.

    """
    tip = models.CharField(max_length=20, default='')
    opis = models.CharField(max_length=100, default='')
    znesek = models.FloatField()
    kategorija = models.CharField(max_length=30, default='')
    datum = models.DateTimeField(default=datetime.now)
    banka_denarnica = models.CharField(max_length=20, default='')
    stanje = models.ForeignKey(Stanje, on_delete=models.CASCADE)

    def __str__(self):
        return ("{}, {}, {}, {}, {} -- {}".format(self.tip, self.banka_denarnica, self.opis, self.kategorija, self.znesek, self.stanje))


class Cilj(models.Model):
    """ Class representing Cilj.

    This is Cilj model, each User can have more Ciljs.

    """
    opis = models.CharField(max_length=150, default='')
    vrednost = models.FloatField()
    trenutno_privarcevano = models.FloatField(default=0)
    od_datuma = models.DateTimeField(default=datetime.now)
    do_datuma = models.DateTimeField()
    uporabnik = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ("{}, {}/{}, {}-{}".format(self.opis, self.trenutno_privarcevano, self.vrednost, self.od_datuma, self.do_datuma))

    def is_close_to_end(self):
        """ Checks if goal is close to an end.

        Returns True if goal is less than a week from now or is already over, otherwise False.

        """
        return timezone.now() + timedelta(days=7) >=  self.do_datuma

    def is_accomplished(self):
        """ Checks if goal is already acomplished.

        Returns True if goal has gathered enough money, otherwise False.

        """
        return self.trenutno_privarcevano >= self.vrednost
