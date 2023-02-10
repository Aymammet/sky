from django.contrib import admin
from .models import User

# Register your models here.
class Admin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email')

admin.site.register(User, Admin)
# Register your models here.
