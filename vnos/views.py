from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from .service import *


@login_required
def vnos(request):
    return render(request, 'vnos/vnos_home.html')


@login_required
def dodaj(request):
    add_data(request)
    return render(request, 'vnos/vnos_home.html')


@login_required
def dodaj_cilj(request):
    add_goal(request)
    return render(request, 'vnos/vnos_home.html')


@login_required
def dodaj_cilju(request):
    add_to_goal(request)
    return render(request, 'vnos/vnos_home.html')