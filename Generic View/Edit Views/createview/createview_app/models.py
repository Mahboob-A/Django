from django.db import models
from django.urls import reverse


class Students(models.Model): 
        first_name = models.CharField(max_length=15)
        middle_name = models.CharField(max_length=15, null=True, blank=True)
        last_name = models.CharField(max_length=15)
        roll = models.IntegerField()
        email = models.EmailField()
        class_name = models.CharField(max_length=15)
        section = models.CharField(max_length=2)
        
        # just redirects to the url here without passing the primary key of newly created db object 
        # def get_absolute_url(self): 
        #         return reverse('thank_you')
        
        # here also passing the pk of the newly created object 
        def get_absolute_url(self):
            return reverse("detail", kwargs={"pk": self.pk})
        


class Teacher(models.Model):

        name = models.CharField(max_length=15)
        email = models.EmailField(max_length=30)
        password = models.CharField(max_length=15)
    

        class Meta:
                verbose_name = ("Teacher")
                verbose_name_plural = ("Teachers")

        def __str__(self):
                return self.name

        def get_absolute_url(self):
                return reverse("detail") #, kwargs={"pk": self.pk})  only senf when the pk is necessary (if pk is being send, then the link should be receiving a pk)
                # if get_absolute_url(self) this method is declared in the model, then success_url is not needed to define.     
                
                
class SchoolStaff(models.Model):

        name = models.CharField(max_length=15)
        email = models.EmailField(max_length=30)
        password = models.CharField(max_length=15)


        class Meta:
                verbose_name = ("SchoolStaff")
                verbose_name_plural = ("SchoolStaffs")

        def __str__(self):
                return self.name

        def get_absolute_url(self):
                return reverse("thank_you") #kwargs={"pk": self.pk})  # redirecting to thank you page 

                
