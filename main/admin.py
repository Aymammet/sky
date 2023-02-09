from django.contrib import admin
from profiles.models import User

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email')

admin.site.register(User, Admin)