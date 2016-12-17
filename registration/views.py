from django.shortcuts import render


def registration(request):
    return render(request, 'registration/registration_home.html')


def index(request):
    return render(request, 'index/index_home.html')


def vnos(request):
    return render(request, 'vnos/vnos_home.html')


def pregled(request):
    return render(request, 'pregled/pregled_home.html')


def vizualizacija(request):
    return render(request, 'vizualizacija/vizualizacija_home.html')