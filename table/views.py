from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def day_tasks(requests, day):
    daily_task = Task.objects.get(day=day)
    return HttpResponse(f"{day} kungi task : {daily_task.task}")