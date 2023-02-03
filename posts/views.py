from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def posts(request):
    return render(request, 'main.html')

def post_detail(request):
    return HttpResponse("Hello post detail page!")

def post_edit(request):
    return render(request, 'post-edit.html')

def post_create(request):
    return render(request, 'post-create.html')