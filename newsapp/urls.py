from unicodedata import name
from django import views
from django.urls import path
from .views import *
from newsapp import views

app_name = "newsapp"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>', DetailView.as_view() ,name = 'detail'),
    path('categories', CategoriesView.as_view() ,name = 'catagories'),
    path('categories/<int:pk>', CategoryView.as_view() ,name = 'catagory'),
]