from django.urls import path
from .views import CustomRegisterView
from .views import login

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', CustomRegisterView.as_view(), name='register'),
]