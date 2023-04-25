# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.core.exceptions import ValidationError
from profiles.models import User
from django.urls import reverse_lazy
from .forms import UserForm
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
     template_name = 'login.html'
     success_url = reverse_lazy('posts')


     def form_invalid(self, form):
          username = self.request.POST.get('username') 
          try:
               user = User.objects.get(username=username)
               form.add_error("password", "The password is wrong")
          except User.DoesNotExist:
               form.add_error("username", "This user does not exist")
          context = {'form': form}
          return render(self.request, self.template_name, context)


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
                    return render(request, self.template_name, {'form': form})
               if form.is_valid():
                    user = form.save(commit=False)
                    password = form.cleaned_data['password']
                    user.set_password(password)
                    user.save()
                    return redirect('login')
               return render(request, self.template_name, {'form': form})
          