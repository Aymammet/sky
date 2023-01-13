from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('detail/', views.post_detail, name='post_detail'),
    
]