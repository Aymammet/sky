from django.urls import path
from .views import CustomRegisterView
from .views import login, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
]