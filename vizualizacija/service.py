import datetime
import json
from django.utils.timezone import make_naive


def show_visual(request):
    dropdown = request.POST['dropdown']
    obdobje = request.POST['obdobje']

    danes = datetime.datetime.now()
    stevilo_dni = 0
    if (obdobje == "teden"):
        stevilo_dni = 7
    elif (obdobje == "mesec"):
        stevilo_dni = 31
    elif (obdobje == "leto"):
        stevilo_dni = 365

    if (dropdown == "wallet"):
        stanje = request.user.stanje_set.filter(tip='denarnica')[0]
    elif (dropdown == "bank"):
        stanje = request.user.stanje_set.filter(tip='banka')[0]
    elif (dropdown == "wallet_and_bank"):
        stanji = request.user.stanje_set.all()

    stanja_denarnica = []
    stanja_banka = []
    stanja_skupaj = []

    if ('stanje' in locals()):
        izdatki_prejemki = list(stanje.izdatekprejemek_set.all().order_by('datum'))
    else:
        izdatki_prejemki_1 = list(stanji[0].izdatekprejemek_set.all().order_by('datum'))
        izdatki_prejemki_2 = list(stanji[1].izdatekprejemek_set.all().order_by('datum'))
        izdatki_prejemki = izdatki_prejemki_1 + izdatki_prejemki_2


    i = 0
    while (i < len(izdatki_prejemki)):
        if ((danes - make_naive(izdatki_prejemki[i].datum)).days > stevilo_dni):
            izdatki_prejemki.pop(i)
            i -= 1

        i += 1

    print(izdatki_prejemki)

    for vnos in izdatki_prejemki:
        znesek = vnos.znesek
        datum = make_naive(vnos.datum)
        if (vnos.banka_denarnica == "banka"):
            if (vnos.tip == "prejemek"):
                stanja_banka.append(["+", znesek, datum])
                stanja_skupaj.append(["+", znesek, datum])
            else:
                stanja_banka.append(["-", znesek, datum])
                stanja_skupaj.append(["-", znesek, datum])
        elif(vnos.banka_denarnica == "denarnica"):
            if (vnos.tip == "prejemek"):
                stanja_denarnica.append(["+", znesek, datum])
                stanja_skupaj.append(["+", znesek, datum])
            else:
                stanja_denarnica.append(["-", znesek, datum])
                stanja_skupaj.append(["-", znesek, datum])

    if (dropdown == "wallet"):
        stanja_denarnica = procces_list(stanja_denarnica)
        json_data = prepare_visual_data(danes, stevilo_dni, stanja_denarnica, dropdown)
        print(stanja_denarnica)
    elif (dropdown == "bank"):
        stanja_banka = procces_list(stanja_banka)
        json_data = prepare_visual_data(danes, stevilo_dni, stanja_banka, dropdown)
        print(stanja_banka)
    elif (dropdown == "wallet_and_bank"):
        stanja_skupaj = procces_list(stanja_skupaj)
        json_data = prepare_visual_data(danes, stevilo_dni, stanja_skupaj, dropdown)
        print(stanja_skupaj)

    return json_data


def procces_list(data):
    podatki = []
    stanje = 0

    for item in data:
        znesek = item[1]
        datum = item[2]
        if(item[0] == '+'):
            stanje += znesek
        elif (item[0] == '-'):
            stanje -= znesek

        podatki.append([stanje, datum])

    return podatki


def prepare_visual_data(danes, stevilo_dni, data, dropdown):
    date_data = {}

    for item in data:
        dan = str(stevilo_dni - (danes - item[1]).days)
        date_data[dan] = [str(item[1]), item[0]]

    date_data["stevilo_dni"] = stevilo_dni
    date_data["banka_denarnica"] = dropdown

    json_data = json.dumps(date_data, ensure_ascii=False)
    return json_data


