from django.contrib import admin

from course.models import Student

# Register your models here.

# ModelAdmin Class || vid - 37 

# A. Registering Model Without using decorator to register the model class 
# 1. create the ModelAdmin class 
# class StudentAdmin(admin.ModelAdmin):
#         list_display = ('id', 'stid', 'stname', 'stclass', 'stemail', 'stpas', 'staddress')
        
# # 2. Now register the model and the ModelAdmin class 
# admin.site.register(Student, StudentAdmin)


# B. Registering Model With Decorator 

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
        list_display = ('id', 'stid', 'stname', 'stclass', 'stemail', 'stpas', 'staddress')
        
# No more need to register like admin.site.register(Model Class, ModelAdminClass) here. 