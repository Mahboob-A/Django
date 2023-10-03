from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .models import Customers

'''
we will have a form class. and FormView will show the form. If we have a Model, we can 
use form_valid(form) method and save the data into it inside the method. 

'''

class ContactFormView(FormView): 
        template_name = 'formapp/contact_form.html'
        form_class = ContactForm  
        success_url = '/thank-you/'   # this is seperate view's link (for httpresponceredirect, this is not required to be placed)
        
        # to extract the data 
        def form_valid(self, form): 
                # print(form)
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                mobile_no = form.cleaned_data['mobile_no']
                
                # if modelform is used 
                # customer = form.save(commit=False)  # Create a new instance without saving to the database yet
                # customer.save()  # Save the customer object to the database
                
                # if form api is used 
                # customer = Customers(name=name, email=email, mobile_no=mobile_no)
                # customer.save()
                
                customer = Customers(name=name, email=email, mobile_no=mobile_no)
                customer.save()
                
                # this will redirect to success_url (must need is no http responses are made)
                return super().form_valid(form)
        
                # just a http responce (doesnot need success_url)
                # return HttpResponse('Success!')
                
                # this is also seperate views link. if this is used, then super should not be called 
                # return HttpResponseRedirect('thank-you')



class ThankYouTemplateView(TemplateView): 
        template_name = 'formapp/thank_you.html'


