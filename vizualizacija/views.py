from django.shortcuts import render


def vizualizacija(request):
    return render(request, 'vizualizacija/vizualizacija_home.html')