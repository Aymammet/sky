from django.db import models
from profiles.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=500, blank=False, validators=[MinLengthValidator(3)])
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='post_images', max_length=100, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
    total_likes = models.PositiveIntegerField(default=0)
    total_dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title  