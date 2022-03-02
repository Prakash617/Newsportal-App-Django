from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(
    [Catagories,Author,News,Sub_New])

