from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

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
            new_user = User.objects.create_user(username=usr, email=None, password=passwd_1)

            if (usr.startswith('marko')):
                g = Group.objects.get_or_create(name="MarkoUsers")
                if (Permission.objects.count() == 30):
                    content_type = ContentType.objects.get_for_model(IzdatekPrejemek)
                    permission = Permission.objects.create(
                        codename='can_visualize',
                        name='Can See Visual Representation',
                        content_type=content_type,
                    )
                    group = Group.objects.get(name='MarkoUsers')
                    group.permissions.set([permission])
                else:
                    print("else... more than zero permissions")
            else:
                g = Group.objects.get_or_create(name="OtherUsers")
                group = Group.objects.get(name='OtherUsers')

            group.user_set.add(new_user)

            new_user.stanje_set.create(tip="banka", stanje=0.0)
            new_user.stanje_set.create(tip="denarnica", stanje=0.0)

            messages.error(request, 'User registered.')
            print("\nUser registered.\n")
            return HttpResponseRedirect(reverse('registration'))
        else:
            messages.error(request, 'This username is already taken.')
            print("\nThis username is already taken.\n")
            return HttpResponseRedirect(reverse('registration'))
    else:
        messages.error(request, 'Passwords are not the same or username is not longer than 5 characters or captcha is not clicked.')
        print("\nPasswords are not the same or username is not longer than 5 characters or captcha is not clicked.\n")
        return HttpResponseRedirect(reverse('registration'))





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

