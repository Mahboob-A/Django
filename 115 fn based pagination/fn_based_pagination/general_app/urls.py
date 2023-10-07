
from django.urls import path 

from .views import show_blog_posts,ShowBlogPostsAPI

urlpatterns = [
        path('', show_blog_posts, name='show_blog_posts'),
        path('api/', ShowBlogPostsAPI.as_view(), name='show_blog_posts_api'),
]
