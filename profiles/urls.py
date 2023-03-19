from django.urls import path
from . import views
from .views import UserDetailView, UserUpdateView


urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('edit/', UserUpdateView.as_view(), name='profile-edit'),
]