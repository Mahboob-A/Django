
from django import forms 
from django.core.validators import RegexValidator

name_validator = RegexValidator(
    regex=r'^[a-zA-Z]*$',
    message='Name should only contain letters.',
)

class CharFieldExamples(forms.Form): 
        name = forms.CharField(
                        min_length=3, max_length=10, error_messages={'required' : 'Please provide your name'}, #validators=[name_validator],
                )
        
        roll = forms.IntegerField(min_value=10, max_value=20, error_messages={'required' : 'Value must be >= 10 and <=20'})

        email = forms.EmailField(max_length=100, error_messages={'required' : 'Enter Email'})
        
        agree = forms.BooleanField(label_suffix=' ', required=False, label='I agree', error_messages={'required' : 'Please agree'},)
        
