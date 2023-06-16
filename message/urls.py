from django.urls import path
from .views import RoomsView

app_name = 'message'

urlpatterns = [
    path('', RoomsView.as_view(), name='rooms'),
]