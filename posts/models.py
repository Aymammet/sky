from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Post(AbstractUser):
    title = models.CharField(max_length=50, blank=False, null=True)
    owner = models.CharField(max_length=500, blank=False, null=True)

    def __str__(self):
        return self.title