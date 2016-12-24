from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.registration, name="registration"),
    url(r'^registracija.html$', views.registration, name="registration_html"),
    url(r'^logout$', views.logout_user, name="logout"),
]