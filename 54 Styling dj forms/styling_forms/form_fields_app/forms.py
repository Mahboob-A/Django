
from django import forms 
from django.core.validators import RegexValidator

name_validator = RegexValidator(
    regex=r'^[a-zA-Z]*$',
    message='Name should only contain letters.',
)

class CharFieldExamples(forms.Form): 
        '''
        name = forms.CharField()  ===> standalone this is required 
        error_messages ===> pass a dict 
        empty_value = value ===> allows to submit without any value (need to give a default value. this makes required = False) 
        widget = renders as Text in HTML 
        stripe = False. (stripe = True as default. stripe trims the trailing white spaces from the input)
        
        '''
        name = forms.CharField(
                        min_length=3, max_length=10, error_messages={'required' : 'Please provide your name'}, #validators=[name_validator],
                )
        
        roll = forms.IntegerField(min_value=10, max_value=20, error_messages={'required' : 'Value must be >= 10 and <=20'})
        
        price = forms.DecimalField(min_value=10, max_value=20, max_digits=3, decimal_places=1)
        rate = forms.DecimalField(min_value=10, max_value=20, max_digits=3, decimal_places=1)
        
        agree = forms.BooleanField(label_suffix=' ', label='I agree', error_messages={'required' : 'Please agree'},)
        
