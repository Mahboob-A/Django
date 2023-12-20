from django.db import models

# Create your models here.

class BlogPost(models.Model): 
        name = models.CharField(max_length=100)
        content = models.TextField(max_length=500)
        pub_date = models.DateTimeField(auto_now_add=True)
        last_edited = models.DateTimeField(auto_now=True)
        
        def __str__(self) -> str:
                return self.name 
        
        