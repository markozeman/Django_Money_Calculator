from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^.html$', views.vnos, name="vnos"),
    url(r'^.html/dodaj$', views.dodaj, name="dodaj"),
    url(r'^.html/dodajcilj$', views.dodaj_cilj, name="dodaj_cilj"),
    url(r'^.html/dodajcilju$', views.dodaj_cilju, name="dodaj_cilju"),
]