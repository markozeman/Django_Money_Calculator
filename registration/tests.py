import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Stanje, Cilj


class Tests(TestCase):
    def test_cilj_is_close_to_end(self):
        """
        is_close_to_end() should return True, if the final date is one week or less from now; False otherwise.
        """
        cilj_just_started = Cilj(do_datuma = timezone.now() + datetime.timedelta(days=30))
        cilj_close_to_end = Cilj(do_datuma = timezone.now() + datetime.timedelta(days=3))

        self.assertIs(cilj_just_started.is_close_to_end(), False)
        self.assertIs(cilj_close_to_end.is_close_to_end(), True)


    def test_cilj_is_accomplished(self):
        """
        is_accomplished() should return True, if you saved enough money for goal; False otherwise.
        """
        cilj_accomplished = Cilj(vrednost = 500.0, trenutno_privarcevano = 500.0)
        cilj_accomplished_2 = Cilj(vrednost = 500.0, trenutno_privarcevano = 510.0)
        cilj_in_progress = Cilj(vrednost = 100.0, trenutno_privarcevano = 20.0)

        self.assertIs(cilj_accomplished.is_accomplished(), True)
        self.assertIs(cilj_accomplished_2.is_accomplished(), True)
        self.assertIs(cilj_in_progress.is_accomplished(), False)


    def test_stanje_is_negative(self):
        """
        is_negative() should return True, if 'stanje' of the user is negative; False otherwise.
        """
        stanje_positive = Stanje(stanje = 150.0)
        stanje_negative = Stanje(stanje = -20.0)

        self.assertIs(stanje_positive.is_negative(), False)
        self.assertIs(stanje_negative.is_negative(), True)