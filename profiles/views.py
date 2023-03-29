from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView, UpdateView
from .models import User
from posts.models import Post
from django.urls import reverse_lazy


class UserDetailView(DetailView):
    model = User
    template_name = 'profile-details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(owner=self.object).order_by('-created_date', '-created_time')
        return context


class UserUpdateView(UpdateView):
    model = User
    fields = ['username','first_name', 'last_name', 'profession', 'bio', 'profile_image']
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