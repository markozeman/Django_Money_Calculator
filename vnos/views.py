from django.shortcuts import render
from .service import *


def vnos(request):
    return render(request, 'vnos/vnos_home.html')


def dodaj(request):
    add_data(request)
    return render(request, 'vnos/vnos_home.html')


def dodaj_cilj(request):
    add_goal(request)
    return render(request, 'vnos/vnos_home.html')


def dodaj_cilju(request):
    add_to_goal(request)
    return render(request, 'vnos/vnos_home.html')