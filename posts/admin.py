from django.contrib import admin
from .models import Post

# Register your models here.
class MyPost(admin.ModelAdmin):
    list_display = ('title', 'owner', 'image','created_date', 'created_time', 'total_likes')

admin.site.register(Post, MyPost)