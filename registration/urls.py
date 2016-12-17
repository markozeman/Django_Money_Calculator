from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.registration, name="registration"),
    url(r'^registracija.html$', views.registration, name="registration"),
    url(r'^index.html$', views.index, name="index"),
    url(r'^vnos.html$', views.vnos, name="vnos"),
    url(r'^pregled.html$', views.pregled, name="pregled"),
    url(r'^vizualizacija.html$', views.vizualizacija, name="vizualizacija"),
]