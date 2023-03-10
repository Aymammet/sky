from django.shortcuts import render, redirect
from django.http import HttpResponse
from profiles.models import User
from .models import Post
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .form import PostForm


# Create your views here.
class PostListView(ListView):
     model = Post
     template_name = 'main.html'
     context_object_name = 'posts'

     def get_queryset(self):
          base_query = super().get_queryset()
          data = base_query.order_by('-created_date', '-created_time')
          return data


class PostCreateview(CreateView):
    model = Post
    template_name = 'post-create.html'
    context_object_name = 'post'
    fields = ['title', 'image']
    success_url = reverse_lazy('posts')
    form = PostForm

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, 'login.html')
        
    def form_valid(self, form):
        myobj = form.save(commit=False)
        myobj.owner = self.request.user
        return super().form_valid(form)
    

def post_detail(request):
    return HttpResponse("Hello post detail page!")

def post_edit(request):
    return render(request, 'post-edit.html')




