from django.shortcuts import render, redirect, get_object_or_404 
from django.views.generic import DetailView, UpdateView
from .models import User
from posts.models import Post
from django.urls import reverse_lazy, reverse
from django.utils.dateformat import DateFormat
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


def error_404(request, exception):
     return render(request, '404.html', status=404)

class UserDetailView(DetailView):
    model = User
    template_name = 'profile-details.html'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(owner=self.object).order_by('-created_date', '-created_time')
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['profile_image','first_name', 'last_name', 'gender', 'profession', 'bio', 'birth_date', ]
    template_name = 'profile-edit.html'
    success_url = reverse_lazy('profile-edit.html')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user != self.get_object():
            return redirect(reverse('profile-edit', kwargs={'pk': self.request.user.pk}))
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(User, pk=pk)
        return obj

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
