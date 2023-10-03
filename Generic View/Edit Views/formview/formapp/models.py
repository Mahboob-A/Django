from django.db import models

# Create your models here.
class Customers(models.Model): 
        name = models.CharField(max_length=30)
        email = models.EmailField(max_length=50)
        mobile_no = models.CharField(max_length=15)