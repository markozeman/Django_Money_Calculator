from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from .service import *


@login_required
def vizualizacija(request):
    return render(request, 'vizualizacija/vizualizacija_home.html')


@login_required
@permission_required('registration.can_visualize', raise_exception=True)
def prikaz(request):
    json_data = show_visual(request)
    return render(request, 'vizualizacija/vizualizacija_home.html', {"json_data": json_data})