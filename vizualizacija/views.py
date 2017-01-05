from django.shortcuts import render
from .service import *


def vizualizacija(request):
    return render(request, 'vizualizacija/vizualizacija_home.html')


def prikaz(request):
    json_data = show_visual(request)
    return render(request, 'vizualizacija/vizualizacija_home.html', {"json_data": json_data})