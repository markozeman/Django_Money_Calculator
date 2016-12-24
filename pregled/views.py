from django.shortcuts import render


def pregled(request):
    return render(request, 'pregled/pregled_home.html')
