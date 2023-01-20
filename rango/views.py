from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!")

def about():
    return HttpResponse("Rango says here is the  <a href='/rango/about/'>about</a>  page" )