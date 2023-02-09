from django.db import models
from profiles.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    total_likes = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title