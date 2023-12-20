
from django.shortcuts import render


# Create your views here.
# model class 
from enroll.models import StudentEnrollModel

from enroll.forms import StudentEnrollForm, StudentEnrollForm2, StudentEnrollFormWidget

# fucn for models data show 
def show_enroll_data(request):
        enroll_obj = StudentEnrollModel.objects.all()
        return render(request, 'enroll/show-enroll-data.html', {'show_enroll_data_obj' : enroll_obj})

# func to show the form 
def show_form(request):
        stud_form_obj = StudentEnrollForm()
        return render(request, 'enroll/show-form.html', {'stud_form_obj' : stud_form_obj})


# views for the StudentEnrollForm2 from class to demonstrate the Form Fields Argument 
def show_form_2(request):
        # forms.py eo initial deowa ache, but ekhaneo initil deowa thakle ei ta survive korbe karon ei tar precedence besi 
        stud_form_obj2 = StudentEnrollForm2(initial={'name' : 'YuriousQurious'})
        return render(request, 'enroll/show-form-2.html', {'stud_form_obj2' : stud_form_obj2})

def show_form_widget(request):
        stud_form_widget_obj = StudentEnrollFormWidget()
        return render(request, 'enroll/show-form-widget.html', {'stud_form_widget_obj' : stud_form_widget_obj})
        