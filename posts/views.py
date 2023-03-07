from django.shortcuts import render, redirect
from django.http import HttpResponse
from profiles.models import User
from .models import Post
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .admin import MyPost


# Create your views here.
class PostListView(ListView):
     model = Post
     template_name = 'main.html'
     context_object_name = 'posts'

     def get_queryset(self):
          base_query = super().get_queryset()
          data = base_query.order_by('created_date')
          return data


class PostCreateview(CreateView):
    model = Post
    template_name = 'post-create.html'
    context_object_name = 'post'
    fields = ['title', 'image']
    success_url = reverse_lazy
    form = MyPost

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, 'login.html')
        
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)





def post_detail(request):
    return HttpResponse("Hello post detail page!")

def post_edit(request):
    return render(request, 'post-edit.html')




