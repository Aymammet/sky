from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
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

def profile_edit(request):
    return HttpResponse("Hello profile_edit page!")