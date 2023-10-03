from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import StudentRegistration
from .models import User
# Create your views here.
from django.views.generic.base import TemplateView, RedirectView  # we can also import view form here 
from django.views import View

'''
080723, Saturday, 05.00 pm 
Panchayat Election day 2023.
Revisoin of class based views. 
'''

''' this class based view will add and show items ( we can create seperate create view for add 
and list view for showing data) '''
class UserAddAndShowView(TemplateView): 
  template_name = 'enroll/addandshow.html'
  
  # GET request 
  def get_context_data(self, *args, **kwargs): 
    context = super().get_context_data(*args, **kwargs)
    form = StudentRegistration()
    students = User.objects.all()
    context = {'form' : form,  'stu' : students}
    return context
    
  def post(self, request): 
    form = StudentRegistration(request.POST or None)
    if form.is_valid():
      # we can directly use form.save 
      form.save() 
      # also we can get the data form the cleaned_data and create an instance of the model and then instance.save 
      # both will work (but crating instance is much better)
      # name = form.cleaned_data['name']
      # email = form.cleaned_data['email']
      # passwd = form.cleaned_data['password']
      # new_user = User(name=name, email=email, password=passwd)
      # new_user.save()
      # return HttpResponse('<h1>Successfully Added</h1>')
      return HttpResponseRedirect('/')
      


''' this class based view is responsible for deleting items'''
class UserDeleteView(RedirectView): 
  url = '/'
  
  def get_redirect_url(self, *args, **kwargs):    # kwargs will hold the any data passed form the url 
    # print(kwargs)
    user_id = kwargs['id']
    User.objects.get(pk=user_id).delete()
    a = super().get_redirect_url(*args, **kwargs)
    # print(a)
    return a  # here a return '/' the value stored in the url variable 
    # return super().get_redirect_url(*args, **kwargs) # This actullly returns the value of the url variable 
  
 

class UpdateUserView(TemplateView):  # we can also use View here. just the get and post code are same whatever we inherit in this case 
  ''' This is responsible for Updating User Data '''
  
  template_name = 'enroll/updatestudent.html'
  
  def get(self, request, id): 
    user_id = User.objects.get(pk=id)
    form = StudentRegistration(instance=user_id)
    return render(request, self.template_name, {'form' : form})
  
  def post(self, request, id): 
    user_id = User.objects.get(pk=id)
    form = StudentRegistration(request.POST, instance=user_id)
    if form.is_valid(): 
      form.save()
    return HttpResponseRedirect('/')
    
    
  

 
 
 
#  function based views 
 

# This Function Will Add new Item and Show All Items
# def add_show(request):
#  if request.method == 'POST':
#   fm = StudentRegistration(request.POST)
#   if fm.is_valid():
#    nm = fm.cleaned_data['name']
#    em = fm.cleaned_data['email']
#    pw = fm.cleaned_data['password']
#    reg = User(name=nm, email=em, password=pw)
#    reg.save()
#    fm = StudentRegistration()
#  else:
#   fm = StudentRegistration()
#  stud = User.objects.all()
#  return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})

# This Function will Update/Edit
# def update_data(request, id):
#  if request.method == 'POST':
#   pi = User.objects.get(pk=id)
#   fm = StudentRegistration(request.POST, instance=pi)
#   if fm.is_valid():
#    fm.save()
#  else:
#   pi = User.objects.get(pk=id)
#   fm = StudentRegistration(instance=pi)
#  return render(request, 'enroll/updatestudent.html', {'form':fm})

# This Function will Delete
# def delete_data(request, id):
#  if request.method == 'POST':
#   pi = User.objects.get(pk=id)
#   pi.delete()
#   return HttpResponseRedirect('/')