from django.shortcuts import render
from django.http import HttpResponse
from profiles.models import User
from posts.models import Post
from django.views.generic import ListView


# Create your views here.
class PostListView(ListView):
     model = Post
     template_name = 'main.html'

     def get_queryset(self):
          base_query = super().get_queryset()
          data = base_query.order_by('created_date')
          return data

def post_detail(request):
    return HttpResponse("Hello post detail page!")

def post_edit(request):
    return render(request, 'post-edit.html')

def post_create(request):
    return render(request, 'post-create.html')


