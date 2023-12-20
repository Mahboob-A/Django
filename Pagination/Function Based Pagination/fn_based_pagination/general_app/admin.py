from django.contrib import admin

# Register your models here.
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'content', 'pub_date', 'last_edited']