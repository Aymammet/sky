from django.urls import path
from .views import CustomRegisterView, CustomLoginView
from django.contrib.auth.views import LogoutView
from sky import settings


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {"next_page": settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
]