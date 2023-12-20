from django.db import models

# Create your models here.
# this is first django model I am creating 
# 110623, Sunday, 06.00 pm 

class Student(models.Model):
        stid=models.IntegerField()
        stname = models.CharField(max_length=50)
        stclass = models.CharField(max_length=10)
        stemail = models.EmailField(max_length=40)
        stpas = models.CharField(max_length=20)
        # if we add a col after we already created a table, we need to specify default value 
        staddress = models.TextField(default='Demo Address', max_length=200)
        
        
        
        # if ModelAdmin class is used, then no need to use this __str__() method 
        # vid 36 || how to register model class in admin 
        
        # use __str__ to show the desired col in admin interface 
        
        # def __str__(self):
        #         return self.stname 
        
        # id show korle id ta str e conver kore nite hobe na hole non-string error asbe karon string chara link kaj korbe na 
        # def __str__(self):
        #         return str(self.stid) 

        