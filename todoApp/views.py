from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Todo APP</h1></center>'
    )