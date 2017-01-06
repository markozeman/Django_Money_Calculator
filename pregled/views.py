from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from .service import *


@login_required
def pregled(request):
    return render(request, 'pregled/pregled_home.html')


@login_required
def iskanje(request):
    context = search(request)
    return render(request, 'pregled/pregled_home.html', context)