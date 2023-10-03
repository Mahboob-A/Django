
from django import forms 
from .models import SchoolStaff

class SchoolStaffForm(forms.ModelForm): 
        
        class Meta: 
                model = SchoolStaff
                fields = ['name', 'email', 'password']
                widgets = {
                        'name' : forms.TextInput(attrs={'class' : 'user_name', 'placeholder' : 'Enter Your Name'}),
                        'email' : forms.EmailInput(attrs={'class' : 'user_email', 'placeholder' : 'Enter Your Email'}),
                        'password' : forms.PasswordInput( attrs={'class' : 'user_password', 'placeholder' : 'Enter Your Password'}),  
                        # forms.PasswordInput e => render_value = True দিলে  updateview use করলে পাসওয়ার্ড ইনপুট টা  ডট ডট ভাবে দেখাবে , placeholder তখন দেখাবে না 
                        # যেহেতু এখন সেটা দেওয়া নেই, এখন placeholder দেখাবে। 
                }