from django.db import models


# Create your models here.
class Student(models.Model): 
        name = models.CharField(max_length=15)
        roll = models.IntegerField()
        email = models.EmailField(max_length=50)
        agree = models.BooleanField(default=False, blank=False)
