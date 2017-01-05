from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^.html$', views.vizualizacija, name="vizualizacija"),
    url(r'^.html/prikazi$', views.prikaz, name="prikaz"),
]