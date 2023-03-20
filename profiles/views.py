from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, UpdateView
from .models import User
from posts.models import Post


class UserDetailView(DetailView):
    model = User
    template_name = 'profile-details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(owner=self.object)
        return context


class UserUpdateView(UpdateView):
    model = User
    fields = ['username','first_name', 'last_name', 'profession','bio', 'email', 'avatar_pic']
    template_name = 'profile-edit.html'
        
    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        return User.objects.get(id=id)
 
         
    def form_valid(self, fields):
        myprofile = fields.save(commit=False)
        myprofile.owner = self.request.user
        response = super().form_valid(fields)
        return response
    



