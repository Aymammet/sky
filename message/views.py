from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Message, Room
import json
from django.http import JsonResponse
from profiles.models import User
from django.core import serializers

# Create your views here.
class RoomsView(LoginRequiredMixin, ListView):
    template_name = "rooms.html"
    model = Message

def get_room_id(x, y):
    if int(x) <= int(y):
        return int(x) * 10000 + int(y)
    else:
        return int(y) * 10000 + int(x)

    
class MessageRoomView(ListView):
    model = Message

    def get(self, request):
        receiver_pk = request.GET.get('receiver')
        current_room_id = get_room_id(request.user.pk, receiver_pk)
        if Room.objects.filter(room_id = current_room_id).exists():
            room = Room.objects.get(room_id = current_room_id)
        else:
            room = Room.objects.create(room_id = current_room_id)
            room.save()
        all_messages = Message.objects.filter(room_id = room)
        messages = list(all_messages.values('content','date', 'sender', 'receiver'))
        return JsonResponse({"messages": messages })
    

class MessageCreateView(CreateView):

    def post(self, request):
        body = json.loads(request.body)
        new_room_id = get_room_id(request.user.pk, body['receiver_id'])
        if Room.objects.filter(room_id=new_room_id).exists():
            current_room = Room.objects.get(room_id=new_room_id)
        else:
            current_room = Room.objects.create(room_id=new_room_id)
            current_room.save()
        # print(current_room)
        new_message = Message.objects.create(
            room_id = current_room,
            content = body['content'],
            sender = request.user,
            receiver = User.objects.get(pk=body['receiver_id']),
        )
        new_message.save()
        all_messages = Message.objects.filter(room_id = current_room)
        messages = list(all_messages.values('content','date', 'sender', 'receiver'))
        return JsonResponse({"messages": messages })


