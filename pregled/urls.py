from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^.html$', views.pregled, name="pregled"),
]