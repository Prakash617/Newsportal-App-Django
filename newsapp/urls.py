from unicodedata import name
from django import views
from django.urls import path
from .views import *
from newsapp import views

app_name = "newsapp"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>', DetailView.as_view() ,name = 'detail'),
]