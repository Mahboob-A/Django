from django.contrib import admin

# Register your models here.
from .models import Customers

@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'email', 'mobile_no']