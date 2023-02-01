from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile_detail(request):
    return render(request, 'profile-details.html')

def profile_edit(request):
    return HttpResponse("Hello profile_edit page!")