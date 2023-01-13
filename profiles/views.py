from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile_detail(request):
    return HttpResponse("Hello profile_detail page!")

def profile_edit(request):
    return HttpResponse("Hello profile_edit page!")