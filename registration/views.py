from django.shortcuts import render
from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required, permission_required

from .service import *


def registration(request):
    if (request.POST.get("register")):
        return register_user(request)

    elif (request.POST.get("sign_in")):
        return login_user(request)

    return render(request, 'registration/registration_home.html')


@login_required
def logout_user(request):
  logout(request)
  print("Logged out")
  return HttpResponseRedirect(reverse('registration'))
