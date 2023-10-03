from django.db import models


# Create your models here.

class StudentEnrollModel(models.Model):
        first_name = models.CharField(max_length=25)
        last_name = models.CharField(max_length=25)
        email = models.EmailField()
        phone_no = models.CharField(max_length=13)
        address = models.TextField()
        initial_amount = models.IntegerField() 
        
        
