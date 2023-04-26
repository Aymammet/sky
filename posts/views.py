from django.shortcuts import render, redirect
from profiles.models import User
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(LoginRequiredMixin, ListView): 
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by('-created_date', '-created_time')
        return data
    
      
class PostEditView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post-edit.html'
    context_object_name = 'post'
    fields = ['title', 'image']
    success_url = reverse_lazy('posts')
    form = PostForm
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        id = self.kwargs.get('pk')
        return Post.objects.get(id=id)
             
    def form_valid(self, form):
        mypost = form.save(commit=False)
        mypost.owner = self.request.user
        response = super().form_valid(form)
        return response
    
    def test_func(self):
        post = self.get_object()
        return post.owner == self.request.user
    
    def handle_no_permission(self):
        return render(self.request, '404.html', status=404)
    

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post-delete.html'
    success_url = reverse_lazy('posts')
    login_url = reverse_lazy('login')

    def test_func(self):
        post = self.get_object()
        return post.owner == self.request.user
    
    def handle_no_permission(self):
        return render(self.request, '404.html', status=404)

        
class PostCreateview(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post-create.html'
    context_object_name = 'post'
    fields = ['title', 'image']
    success_url = reverse_lazy('posts')
    form = PostForm
    login_url = reverse_lazy('login')
    
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, 'login.html')
        
    def form_valid(self, form):
        myobj = form.save(commit=False)
        myobj.owner = self.request.user
        return super().form_valid(form)
    