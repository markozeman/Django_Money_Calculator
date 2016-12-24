from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .models import *


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

            uporabnik = Uporabnik(uporabnik=new_user)
            uporabnik.save()

            bancno_stanje = Stanje(tip="banka", stanje=0.0, uporabnik=uporabnik)
            bancno_stanje.save()

            denarnica_stanje = Stanje(tip="denarnica", stanje=0.0, uporabnik=uporabnik)
            denarnica_stanje.save()

            print("\nUser registered.\n")
            return HttpResponseRedirect(reverse('registration'))
        else:
            print("\nThis username is already taken.\n")
            return HttpResponseRedirect(reverse('registration'))
    else:
        print("\nPasswords are not the same or username is not longer than 5 characters or captcha is not clicked.\n")



def login_user(request):
    username = request.POST['up_ime']
    password = request.POST.get('geslo', False)
    password_2 = request.POST.get('geslo_2', False)

    if (password is False and password_2 is False):
        print("Password input is blank.")
    elif (len(password_2 )!= 0):
        password = password_2

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        print("Logged in.")
        return HttpResponseRedirect(reverse('vnos'))
    else:
        print("Invalid login")
        return HttpResponseRedirect(reverse('registration'))

