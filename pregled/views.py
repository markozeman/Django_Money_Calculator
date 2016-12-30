from django.shortcuts import render
from .service import *


def pregled(request):
    return render(request, 'pregled/pregled_home.html')


def iskanje(request):
    context = search(request)
    return render(request, 'pregled/pregled_home.html', context)