# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.core.exceptions import ValidationError
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
          form = self.form_class(request.POST, request.FILES)
          password = request.POST.get('password')
          password2 = request.POST.get('password2')
          if request.user.is_authenticated:
               return redirect('posts')
          else:
               if password != password2:
                    form.add_error("password", "Your password inputs doesn't match, please correct it!")
               # if len(username) < 5 or len(username) > 20:
               #      form.add_error("username", "Your username should be longer than 5 and less than 20 letters & symbols")
               return render(request, self.template_name, {'form': form})
               