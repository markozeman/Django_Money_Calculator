from django.shortcuts import render
from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required, permission_required

from .service import *

import logging
import datetime

logger = logging.getLogger('my_logger')


def registration(request):
    """ Function for register and sign up

    Depends on the submit button user can register or sign up to start using application.

    :param request: HTTP request
    :return: renders HTML page
    """
    if (request.POST.get("register")):
        return register_user(request)

    elif (request.POST.get("sign_in")):
        return login_user(request)

    return render(request, 'registration/registration_home.html')


@login_required
def logout_user(request):
    """ Function for logout

    User is logged out of the application.

    :param request: HTTP request
    :return: renders HTML page
    """
    logout(request)
    print("Logged out")
    logger.debug(
      datetime.datetime.now().strftime("%B %d, %Y - %I:%M%p") + ' -- ' + str(request.user) + ' -- ' + 'Logged out.\n')
    return HttpResponseRedirect(reverse('registration'))
