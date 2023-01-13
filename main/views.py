# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("Hello login page!")

def register(request):
    return HttpResponse("Hello register page!")