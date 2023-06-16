from django.db import models
from django.utils import timezone
from profiles.models import User

# Create your models here.

class Room(models.Model):
    room_id = models.IntegerField()

class Message(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, default=0)
    content = models.TextField(max_length=1500)
    date = models.DateTimeField(default=timezone.now)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='received_messages') # remove this
    
    def __str__(self):
        return self.sender.username + '-->' + self.receiver.username + ':' + self.content[:10]
    
