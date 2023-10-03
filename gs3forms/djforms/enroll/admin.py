from django.contrib import admin

from enroll.models import StudentEnrollModel
# Register your models here.

@admin.register(StudentEnrollModel)
class StudentEnrollAdmin(admin.ModelAdmin):
        list_display = ['first_name', 'last_name', 'email', 'phone_no', 'address', 'initial_amount']
        