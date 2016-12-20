from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import LoginForm
from .models import *


def registration(request):
    if (request.method == 'POST'):
        if (request.POST.get("register")):
            register_user(request)

        elif (request.POST.get("sign_in")):
            login_user(request)

    return render(request, 'registration/registration_home.html')


def index(request):
    return render(request, 'index/index_home.html')


def vnos(request):
    return render(request, 'vnos/vnos_home.html')


def pregled(request):
    return render(request, 'pregled/pregled_home.html')


def vizualizacija(request):
    return render(request, 'vizualizacija/vizualizacija_home.html')





def register_user(request):
    usr = request.POST['up_ime']
    passwd_1 = request.POST['geslo']
    passwd_2 = request.POST['geslo_2']
    captcha = request.POST.get('captcha', False)

    # check if passwords are the same, check if username is at least 6 characters long and captcha clicked
    if (passwd_1 == passwd_2 and len(usr) > 5 and captcha is not False):
        username_taken = False
        all_users = list(User.objects.all())
        for user in all_users:
            if (user.username == usr):
                username_taken = True
                break

        if (not username_taken):
            new_user = User.objects.create_user(usr, None, passwd_1)
            new_user.save()

            bancno_stanje = Stanje("banka", 0.0)
            denarnica_stanje = Stanje("denarnica", 0.0)
            uporabnik = Uporabnik(new_user, bancno_stanje, denarnica_stanje)
            uporabnik.save()

            # TODO
            # save Stanje ???

            # TODO
            # zakaj ne dela uporabnik ???

            print("\nUser registered.\n")
        else:
            print("\nThis username is already taken.\n")
    else:
        print("\nPasswords are not the same or username is not longer than 5 characters or captcha is not clicked.\n")



def login_user(request):
    username = request.POST['up_ime']
    password = request.POST.get('geslo', False)
    password_2 = password = request.POST.get('geslo_2', False)

    if (password is False and password_2 is False):
        print("Password input is blank.")
    if (password_2 is not False):
        password = password_2

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        print("Logged in.")
        # Redirect to a success page.
    else:
        # Return an 'invalid login' error message.
        print("Invalid login")



def logout_user(request):
  logout(request)
  return HttpResponseRedirect(reverse('registracija'))