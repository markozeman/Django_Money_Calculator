import datetime
from django.utils.timezone import make_naive

import logging
import datetime

logger = logging.getLogger('my_logger')


def search(request):
    """ Searches in database for given input

    Reads user input and searches database and returns the data in structured form as bullets

    :param request: HTTP request
    :return: dictionary with keys 'izdatki', 'prejemki' and 'cilji'
    """
    select_opcija = request.POST['select_opcija']
    kategorija = request.POST['kategorija']
    obdobje = request.POST['obdobje']

    danes = datetime.datetime.now()
    stevilo_dni = 0
    if (obdobje == "teden"):
        stevilo_dni = 7
    elif (obdobje == "mesec"):
        stevilo_dni = 30
    elif (obdobje == "leto"):
        stevilo_dni = 365

    context = {
        'izdatki': [],
        'prejemki': [],
        'cilji': [],
    }

    if (select_opcija == "wallet"):
        stanje = request.user.stanje_set.filter(tip='denarnica')[0]
    elif (select_opcija == "bank"):
        stanje = request.user.stanje_set.filter(tip='banka')[0]
    elif (select_opcija == "goals"):
        uporabnik = request.user
        cilji = uporabnik.cilj_set.order_by('-do_datuma')

        context['cilji'] = cilji

        for c in cilji:
            print(c)

        return context


    if (kategorija == "vsi_izdatki"):
        izdatki = list(stanje.izdatekprejemek_set.filter(tip='izdatek'))

        if (len(izdatki) > 0):
            i = 0
            while (i < len(izdatki)):
                if ((danes - make_naive(izdatki[i].datum)).days > stevilo_dni):
                    izdatki.pop(i)
                    i -= 1

                i += 1

        context['izdatki'] = izdatki

        for i in izdatki:
            print(i)

    elif (kategorija == "vsi_prejemki"):
        prejemki = list(stanje.izdatekprejemek_set.filter(tip='prejemek'))

        if (len(prejemki) > 0):
            i = 0
            while (i < len(prejemki)):
                if ((danes - make_naive(prejemki[i].datum)).days > stevilo_dni):
                    prejemki.pop(i)
                    i -= 1

                i += 1

        context['prejemki'] = prejemki

        for i in prejemki:
            print(i)

    else:
        izdatki_kategorije = list(stanje.izdatekprejemek_set.filter(kategorija=kategorija, tip='izdatek'))
        prejemki_kategorije = list(stanje.izdatekprejemek_set.filter(kategorija=kategorija, tip='prejemek'))

        print(izdatki_kategorije)
        print(prejemki_kategorije)

        context['izdatki'] = izdatki_kategorije
        context['prejemki'] = prejemki_kategorije

    s = 'Search in ' + select_opcija + " for last " + str(stevilo_dni) + " days for category " + kategorija + ".\n"
    logger.debug(datetime.datetime.now().strftime("%B %d, %Y - %I:%M%p") + ' -- ' + str(request.user) + ' -- ' + s)

    return context
