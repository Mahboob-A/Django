from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms 
from .models import Students, SchoolStaff
from .forms import SchoolStaffForm



class ThankYouTemplateView(TemplateView): 
        template_name = 'deleteview_app/thank_you.html'

''' CreateViews without model form  '''
class StudentCreateView(CreateView): 
        ''' CreateView without any form customaization  '''
        model = Students
        fields = ['first_name', 'middle_name', 'last_name', 'roll', 'email', 'class_name', 'section']
        
        # this class uses the default student_form template 
        
        '''
        here if we want to customize the default form, we can use and override the get_form(self) method
        this will allow customization to the default form. 
        '''

class SchoolStaffCreateView(CreateView):
        ''' CreatView with ModelFrom '''
        form_class = SchoolStaffForm   # no need to define model = model name as it is already defined in the modelform meta class 
        template_name = 'deleteview_app/school_staff.html'
        
        # no success_url is defined here because get_absolute_url is defined in the associated  Schoolstaff model..  
        

''' DELETEVIEW '''
class StudentDeleteView(DeleteView): 
        ''' DeleteView To Delete Model Objects  '''
        model = Students
        success_url = '/thank-you/'
        template_name = 'deleteview_app/student_delete.html'
        
        ''''
        In DeleteView, we need receive a pk in the url and define from which model the data should be deleted. 
        define success_url or define get_absolute_url in the model. 
        
        DeleteView does not return any form. Just in the form tag, pur method = post and give a submit button. that's all. 
        
        The default template name is : modelname_confirm_delete.html 
        if template_name is not defined.  
        '''