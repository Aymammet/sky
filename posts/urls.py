from django.urls import path
from . import views
from .views import PostListView, PostCreateview, PostEditView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('detail/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
    path('create/', PostCreateview.as_view(), name='post_create'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]