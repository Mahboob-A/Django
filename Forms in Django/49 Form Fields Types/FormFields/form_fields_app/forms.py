
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
        
        school_name = forms.CharField() # for validating specific field | v50 
        
        grade = forms.CharField() # for validating all the data using clean method | v51
        
        def clean_school_name(self): 
                school_name = self.cleaned_data.get('school_name')
                print(type(school_name))
                if school_name[0].lower() != 'r': 
                        raise forms.ValidationError('Your school name should begin with R ')
                return school_name
        
        def clean_name(self):  
                name = self.cleaned_data['name']
                if name and not name.isalpha(): 
                        raise forms.ValidationError('Name should be characters')
                return name         
        
        classes = ['i', 'ii', 'iii', 'iv']
        def clean(self): 
                # we can validate all the fields in this method         
                # if all the fields are validated in this method, then if more than one field has error, then it will show errors one by one once the user 
                # corrects the error as if any field raises the error, the validaiton stops there.      
                cleaned_data = super().clean()
                grade = cleaned_data['grade'].lower()
                print("g: ", grade)
                if grade not in self.classes: 
                        raise forms.ValidationError('You must be in primary school')