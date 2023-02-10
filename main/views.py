# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from profiles.models import User
from django.urls import reverse_lazy
from .forms import UserForm

def login(request):
     return render(request, 'login.html')

class CustomRegisterView(CreateView):
     model = User
     form_class = UserForm
     template_name = 'register.html'
     success_url = reverse_lazy('main:login')

     def post(self, request, *args, **kwargs):
          data= request.POST
          # print(data)
          return