from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django import forms 
from .models import Students, Teacher
from .forms import SchoolStaffForm


''' A. WAY 01 OF CREATE VIEW '''

class StudentCreateView(CreateView): 
        ''' A.1. CreateView without any form customaization  '''
        model = Students
        fields = ['first_name', 'middle_name', 'last_name', 'roll', 'email', 'class_name', 'section']
        # success_url = '/add/'  # we can also use get_absolute_url method in the model and pass any data 
        # collected form the url to the linked veiw. 
        # see the get_absolute_url method in the  model 
        

class ThankYouTemplateView(TemplateView): 
        template_name = 'createview_app/thank_you.html'


class StudentDetailView(DetailView): 
        model = Teacher
        template_name = 'createview_app/student_detail_page.html'



class TeacherCreateView(CreateView): 
        ''' A.2.  CreateView with form customization  '''
        model = Teacher
        fields = ['name', 'email', 'password']
        template_name = 'createview_app/teacher.html'  # default is : modelname_detail.html 
        
        def get_form(self): 
                ''' to customize the form, we can override the get_form method '''
                form = super().get_form()
                form.fields['name'].widget = forms.TextInput(attrs={'class' : 'user_name', 'placeholder' : 'Enter Your Name'})
                form.fields['email'].widget = forms.EmailInput(attrs={'class' : 'user_email', 'placeholder' : 'Enter Your Email'})
                form.fields['password'].widget = forms.PasswordInput(attrs={'class' : 'user_password', 'placeholder' : 'Enter Your Password'})
                return form 



''' B. WAY 02 OF CREATE VIEW '''

class SchoolStaffCreateView(CreateView): 
        ''' B.1 CreateView using form_class = ModelFormClass (an easy and mathod, as we are using model form, 
        we should customize the form in the model form itself. So, here no need to customize
        # this doesnot provide default modelname_detail.html template so need to use template_name
        # additionallly we can use get_absolute_url in the model itselt to redirect or we can use success_url in the createview sub class)'''
        
        form_class = SchoolStaffForm
        template_name = 'createview_app/school_staff.html'
        
        # success_url = '/staff/'  # success_url has greater precedence than get_absolute_url i.e if both are defined then success_url will be executed. 
        









