from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('detail/', views.post_detail, name='post_detail'),
    path('post-edit/', views.post_edit, name='post_edit'),
    path('post-create/', views.post_create, name='post_create'),
]