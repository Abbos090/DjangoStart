from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Salom")

def info(request):
    return HttpResponse("Info")