from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('contacts', views.contacts),
    path('', views.home),
    path('publications', views.publications),
    path('publication', views.publication),
    path('css', views.css),
] 
