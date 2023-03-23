from django.urls import path
from . import views
from .views import UserDetailView, UserUpdateView


urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('edit/<int:pk>/', UserUpdateView.as_view(), name='profile-edit'),
]