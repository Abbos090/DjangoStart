from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(requests):
    return HttpResponse("Home page")

def salom(requests):
    return HttpResponse("Assalomu alaykum")