from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from .models import BlogPost
from .serializer import BlogPostSerializer

def show_blog_posts(request): 
        all_blog_posts = BlogPost.objects.all().order_by('id') # Paginator class expects an ordered queryset 
        page_number = request.GET.get('page', 1)
        paginator = Paginator(all_blog_posts, 2, orphans=2) # queryset, and number of items per page 
        paginated_page = paginator.get_page(page_number)
        return render(request, 'general_app/home.html', {'blog_posts' : paginated_page})


class ShowBlogPostsAPI(APIView): 
        def get(self, request): 
                all_blog_posts = BlogPost.objects.all().order_by('id') # Paginator class expects an ordered queryset 
                page_number = request.query_params.get('page', 1)
                paginator = Paginator(all_blog_posts, 2, orphans=2) # queryset, and number of items per page 
                paginated_page = paginator.get_page(page_number)
                serializer = BlogPostSerializer(paginated_page, many=True)
                return Response({'status' : 'success', 'data' : serializer.data}, status=status.HTTP_200_OK)
                
        

