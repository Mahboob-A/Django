from django.shortcuts import render

# Create your views here.
from .forms import StudentRegistrationForm 
from .models import Student

def register_students(request): 
        if request.method == 'POST': 
                form = StudentRegistrationForm(request.POST)
                # do not use the data getting from request.POST
                # always get the data from cleaned_data 
                # request.POST example: 
                # <QueryDict: {'csrfmiddlewaretoken': ['aFFn0N8RSiyu6sg6Sfej3L2xhI5kTgxvGlb9nYmsfqIuG5v0lImOfsdhBgbtwVuP'], 'name': ['abcd'], 'roll': ['110'], 'email': ['abcd@gmail.com'], 'agree': ['on']}>
                print(request.POST)
                print()
                nm = request.POST['name']
                print('nm : ', nm)
                roll = request.POST.get('roll', None)
                print('roll: ', roll)
                agree = request.POST.get('agree',)
                print('agree: ', agree)
                print()
                if form.is_valid(): 
                        print(form.cleaned_data)
                        name = form.cleaned_data['name']
                        print(name)
                        email = form.cleaned_data['email']
                        agree = form.cleaned_data['agree']
                        st = Student(name=name, roll=roll, email=email, agree=agree)
                        st.save()
        else: 
                form = StudentRegistrationForm()
        return render(request, 'school/register.html', {'form' : form})