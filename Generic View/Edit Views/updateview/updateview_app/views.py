from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms 
from .models import Students, SchoolStaff
from .forms import SchoolStaffForm



class ThankYouTemplateView(TemplateView): 
        template_name = 'updateview_app/thank_you.html'

''' CreateViews without model form  '''
class StudentCreateView(CreateView): 
        ''' CreateView without any form customaization  '''
        model = Students
        fields = ['first_name', 'middle_name', 'last_name', 'roll', 'email', 'class_name', 'section']
        
        '''
        here if we want to customize the default form, we can use and override the get_form(self) method
        this will allow customization to the default form. 
        '''

class SchoolStaffCreateView(CreateView):
        ''' CreatView with ModelFrom '''
        form_class = SchoolStaffForm   # no need to define model = model name as it is already defined in the modelform meta class 
        template_name = 'updateview_app/school_staff.html'
        
        # no success_url is defined here because get_absolute_url is defined in the associated  Schoolstaff model..  
        
        
''' Update Views Both ways '''

class StudentUpdateView(UpdateView): 
        ''' updateveiw for StudentCreate create vie '''
        ''' Update View using fields (without model form) This uses default modelname_form.html tempalte '''
        
        model = Students
        fields = ['first_name',  'last_name',  'email', 'class_name']
        success_url = '/thank-you/'
        
        '''
        As this is the update view for student's create view, and assume we have overridden 
        get_form and customized the default form, irrecpective of if we use same template, the customization 
        will not be effective in the updateview. 
        
        so, if we want to customize the default form of updateview also, we should override the get_form(self)
        method in the updateveiw sub-class also. 
        '''



class SchoolStaffUpdateView(UpdateView): 
        
        ''' updateveiw for schoolstaffcreate view '''
        ''' 
        UpdateViews using form_fields (model form)  | Here custom template is needed as no default template 
        is available as form_class is used 
        '''
        model = SchoolStaff   # writing model in Updateview is mandatory irrecpective of CreateView has used fields or form_class 
        # fields = ['name', 'email', 'password']
        form_class = SchoolStaffForm  # can be used form_class or fields (using model form all the customization will be auto applied availlable in the model form)
        template_name = 'updateview_app/school_staff_update.html'  # can be used different templates 
        success_url = '/thank-you/'
        
        '''
        if here model form (form_class) is not used, then we can override the get_form(self) method to apply customization to 
        the default form. 
        '''


