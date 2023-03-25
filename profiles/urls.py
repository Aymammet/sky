from django.urls import path
from . import views
from .views import UserDetailView


urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('edit/', views.profile_edit, name='profile-edit'),
]