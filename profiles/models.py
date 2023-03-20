from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True, validators=[MinLengthValidator(3)])
    email = models.EmailField(unique=True, blank=False)
    profession = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'),('Female', 'Female'),('Other', 'Other')], blank=True)
    avatar_pic = models.ImageField(upload_to='profile_images', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
