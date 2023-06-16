from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Message


# Create your views here.
class RoomsView(LoginRequiredMixin, ListView):
    template_name = "rooms.html"
    model = Message
    

    