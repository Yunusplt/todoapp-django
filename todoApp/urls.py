from django.urls import path
from .views import home
#!MVS

urlpatterns = [
    path('', home ),

]