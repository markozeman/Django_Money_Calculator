import logging
import datetime

logger = logging.getLogger('my_logger')


def add_data(request):
    """ Adds data to the database

    Saves entered data to the database with given form values.

    :param request: HTTP request
    :return: None
    """
    dropdown = request.POST['dropdown']
    opis = request.POST['opis']
    znesek = float(request.POST['znesek'])
    kategorija = request.POST['kategorija']

    if (dropdown == "wallet"):
        stanje = request.user.stanje_set.filter(tip='denarnica')[0]
    elif (dropdown == "bank"):
        stanje = request.user.stanje_set.filter(tip='banka')[0]

    if (request.POST.get("plus")):
        stanje.izdatekprejemek_set.create(tip="prejemek", opis=opis, znesek=znesek, kategorija=kategorija, banka_denarnica=stanje.tip)
        stanje.stanje += znesek
        stanje.save()

    elif (request.POST.get("minus")):
        stanje.izdatekprejemek_set.create(tip="izdatek", opis=opis, znesek=znesek, kategorija=kategorija, banka_denarnica=stanje.tip)
        stanje.stanje -= znesek
        stanje.save()

    logger.debug(
        datetime.datetime.now().strftime("%B %d, %Y - %I:%M%p") + ' -- ' + str(request.user) + ' -- ' + 'Expense or revenue was saved to database.\n')


def add_goal(request):
    """ Adds goal to the database

    Saves entered goal to the database with given form values.

        :param request: HTTP request
        :return: None
    """
    opis_privarcevanja = request.POST['opis_privarcevanja']
    vrednost = float(request.POST['vrednost'])
    datum = request.POST['datum']

    request.user.cilj_set.create(opis=opis_privarcevanja, vrednost=vrednost, do_datuma=datum)

    logger.debug(datetime.datetime.now().strftime("%B %d, %Y - %I:%M%p") + ' -- ' + str(request.user) + ' -- ' + 'Goal saved to database.\n')


def add_to_goal(request):
    """ Adds money to the goal

    Adds given amount of money to the chosen goal and saves changes to the database.

    :param request: HTTP request
    :return: None
    """
    vzemi_iz = request.POST['vzemi_iz']
    vrednost = float(request.POST['vrednost'])
    za_cilj = request.POST['za_cilj']
    opis = "Dodajanje cilju " + za_cilj

    if (vzemi_iz == "wallet"):
        stanje = request.user.stanje_set.filter(tip='denarnica')[0]
    elif (vzemi_iz == "bank"):
        stanje = request.user.stanje_set.filter(tip='banka')[0]

    stanje.izdatekprejemek_set.create(tip="izdatek", opis=opis, znesek=vrednost, kategorija="dodajanje_cilju", banka_denarnica=stanje.tip)
    stanje.stanje -= vrednost
    stanje.save()

    izbrani_cilj = request.user.cilj_set.filter(opis=za_cilj)[0]
    izbrani_cilj.trenutno_privarcevano += vrednost
    izbrani_cilj.save()

    logger.debug(datetime.datetime.now().strftime("%B %d, %Y - %I:%M%p") + ' -- ' + str(request.user) + ' -- ' + 'Added to goal and saved to database.\n')


'''
import requests

req = requests.Request('POST','http://127.0.0.1:8000/vnos.html',headers={'X-Custom':'Test'},data='dropdown=wallet&opis=test_request&znesek=10&kategorija=hrana&plus=Dodaj')
prepared = req.prepare()

s = requests.Session()
s.send(prepared)
'''