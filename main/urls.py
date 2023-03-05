from django.urls import path
from .views import CustomRegisterView
from .views import login
from django.contrib.auth.views import LogoutView
from sky import settings


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), {"next_page": settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
]