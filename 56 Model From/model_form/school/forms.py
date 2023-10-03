from django import forms

from .models import Student


class StudentRegistrationForm(forms.ModelForm): 
        agree = forms.BooleanField(required=False)
        name = forms.CharField(max_length=20)
        class Meta: 
                model = Student
                fields = ['name', 'roll', 'email', 'agree']
                labels = {'name' : 'Your Name', 'roll' : 'Your Roll', 'email' : 'Your Email', 'agree' : 'Do You Agree'} 
                help_text = {'name' : 'Enter Your Full Name'}
                error_messages = {'name' : {'required' : 'Enter Name'},
                                  'roll' : {'required' : 'Enter Roll'}, 
                                  'email' : {'required' : 'Enter Email'},
                                  'agree' : {'required' : 'Please Agree'},
                                }
                widgets = {'name' : forms.TextInput(attrs={'class' : 'nameclass', 'placeholder' : 'Enter Your Name'})}