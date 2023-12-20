
'''
Forms creation in Django. 
130623, Tuesday, 05.00 pm 
Vid - 38 
'''

from django import forms 

# Create a form class 

# Geeky Shows Vid 39 
class StudentRegistration(forms.Form):
        first_name = forms.CharField()     #here max_length is not required as no table in db will be created 
        last_name = forms.CharField()
        phone = forms.CharField()
        email = forms.EmailField()
        