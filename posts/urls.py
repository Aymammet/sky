from django.urls import path
from . import views
from .views import PostListView, PostCreateview, PostEditView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('create/', PostCreateview.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]