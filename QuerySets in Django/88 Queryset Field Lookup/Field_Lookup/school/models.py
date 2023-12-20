from django.db import models

# Create your models here.

class Student(models.Model): 
        name = models.CharField(max_length=30)
        roll = models.IntegerField()
        grade = models.CharField(max_length=5)
        city = models.CharField(max_length=30)
        marks = models.DecimalField(max_digits=5, decimal_places=2)
        admission_date = models.DateTimeField()
        pass_date = models.DateField()
        
        def __srt__(self): 
                return self.name 
