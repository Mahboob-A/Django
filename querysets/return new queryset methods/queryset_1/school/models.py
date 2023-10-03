from django.db import models

# Create your models here.

class Student(models.Model): 
        name = models.CharField(max_length=30)
        class_name = models.CharField(max_length=10)
        roll = models.IntegerField(unique=True, null=False)
        marks = models.IntegerField(default=0)
        pass_date = models.DateField()
        city = models.CharField(max_length=30)