from django.urls import path
from . import views
from .views import PostListView, PostEditView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('detail/', views.post_detail, name='post_detail'),
    path('edit/', PostEditView.as_view(), name='post_edit'),
    path('create/', views.post_create, name='post_create'),
]