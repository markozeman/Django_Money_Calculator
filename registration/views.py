from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .models import *
from .service import *



def registration(request):
    if (request.POST.get("register")):
        return register_user(request)

    elif (request.POST.get("sign_in")):
        return login_user(request)

    return render(request, 'registration/registration_home.html')


def logout_user(request):
  logout(request)
  print("Logged out")
  return HttpResponseRedirect(reverse('registration'))
