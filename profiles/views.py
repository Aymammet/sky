from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, UpdateView
from .models import User
from posts.models import Post
from django.urls import reverse_lazy
from django.utils.dateformat import DateFormat


class UserDetailView(DetailView):
    model = User
    template_name = 'profile-details.html'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(owner=self.object).order_by('-created_date', '-created_time')
        return context


class UserUpdateView(UpdateView):
    model = User
    fields = ['profile_image','first_name', 'last_name', 'gender', 'profession', 'bio', 'birth_date', ]
    template_name = 'profile-edit.html'


    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        return User.objects.get(id=id)
    
    def form_valid(self, form):
        user = form.save(commit=False)
        if user == self.request.user:
            user.save()
            return super().form_valid(form)
        else:
            return redirect('profile-edit.html')
        
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # format the birth_date field as a string
        birth_date = self.object.birth_date
        if birth_date:
            date_format = DateFormat(birth_date)
            context['formatted_birth_date'] = date_format.format('Y-m-d')
        return context
