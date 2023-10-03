
from django import forms 
from .models import SchoolStaff

class SchoolStaffForm(forms.ModelForm): 
        
        class Meta: 
                model = SchoolStaff
                fields = ['name', 'email', 'password']
                widgets = {
                        'name' : forms.TextInput(attrs={'class' : 'user_name', 'placeholder' : 'Enter Your Name'}),
                        'email' : forms.EmailInput(attrs={'class' : 'user_email', 'placeholder' : 'Enter Your Email'}),
                        'password' : forms.PasswordInput(attrs={'class' : 'user_password', 'placeholder' : 'Enter Your Password'}),
                }