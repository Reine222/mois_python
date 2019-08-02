from django.urls import path
from . import views
urlpatterns = [
    path('acceuil', views.home),
    path('home', views.Home),
    path('scrap', views.scrap),
]