from django.shortcuts import render

from .forms import StudentRegistration

# Create your views here.

# vid 39 
''' 
        we can pass auto_id = False, ot True, or "str_%s" 
        str_%s will make the id as str_fieldname 
        
        the default is id_fieldname 
        
        label_suffix => is arguaent diye FieldName er por ( : ) ta bad diye nijer moto 
        char deowa jai. 
        
        initial => initial argument ekta dict nei. dict e fieldname : value hisebe value pass 
        korte hoy. fole oi field name e respected value ta initially show korbe. 
        
'''

# vid 40 
'''
formClassObject.order_fields(fileld_order=['fieldname1', 'fileldname2', ...])

order_fields method field_order parameter receive kore o ete ekta list dite hoy 
field names gulor je order e chai. 

by default - forms.py e je order e field gulo thake sei order ei render hoy 
'''

def register_student(request):
        
       
        # student_registration_obj = StudentRegistration(auto_id="custom_%s", label_suffix='  ', initial={'first_name' : 'Mahboob', 'email' : 'demo@mahboob.com'}) 
        student_registration_obj = StudentRegistration()
        # student_registration_obj.order_fields(field_order=['first_name', 'last_name', 'email', 'phone'])
        return render(request, 'registration/student_registration_display.html', {'student_registration_form' : student_registration_obj})