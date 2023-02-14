# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from profiles.models import User
from django.urls import reverse_lazy
from .forms import UserForm
from posts.views import posts

def login(request):
     return render(request, 'login.html')

class CustomRegisterView(CreateView):
     model = User
     form_class = UserForm
     template_name = 'register.html'
     success_url = reverse_lazy('main:login')

     def get(self, request):
          if request.user.is_authenticated:
               return redirect('posts')
          else:
               return render(request, self.template_name)


     def post(self, request, *args, **kwargs):
          # data= request.POST
          name = request.POST.get('username')
          if request.user.is_authenticated:
               return redirect('posts')
          else:
               return redirect('posts')
               # form = self.form_class(request.POST)
               return