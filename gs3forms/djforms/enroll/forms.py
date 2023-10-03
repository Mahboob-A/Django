#forms.py  

from django import forms 

'''

140623, Wednesday, 10.30 am 
VID - 42 : Loop Form Fields and Loop Hidden and Visible Fields 

'''

class StudentEnrollForm(forms.Form):
        first_name = forms.CharField()
        last_name = forms.CharField()
        email = forms.EmailField()
        phone_no = forms.CharField()
        address = forms.CharField()
        # To make any field hidden, use widget=forms.HiddenInput() in its field parameter 
        initial_amount = forms.IntegerField(widget=forms.HiddenInput()) 
        
# vid 43 : form field argument 
class StudentEnrollForm2(forms.Form):
        # label= argument helps to give custom label name 
        name = forms.CharField(label='Your Name', label_suffix=' > ', initial='Yurious', required=False, disabled=True, 
                               
                               help_text='This form is disabled for now using disabled=True. Thank you for your patience!')
        
        
# vid 44 : form widget in fields 
class StudentEnrollFormWidget(forms.Form):
        name = forms.CharField(label="Your Name " , help_text="Enter Your Name ")
        password = forms.CharField(widget=forms.PasswordInput)  #if attrs is not passed, then it is optional to put bracket 
        profile_pic = forms.CharField(widget=forms.FileInput())   
        would_attend_meeting = forms.CharField(widget=forms.CheckboxInput(attrs={'class' : 'check_box_class', 'id' : 'check_box_id'}))
        address = forms.CharField(widget=forms.Textarea)
        
        