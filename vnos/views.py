from django.shortcuts import render


def vnos(request):
    return render(request, 'vnos/vnos_home.html')