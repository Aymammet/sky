from django.urls import path
from .views import RoomsView, MessageRoomView, MessageCreateView

app_name = 'message'

urlpatterns = [
    path('', RoomsView.as_view(), name='rooms'),
    path('rooms/', MessageRoomView.as_view(), name='message-rooms'),
    path('create/', MessageCreateView.as_view(), name='create-message'),
]