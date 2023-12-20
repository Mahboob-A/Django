from django.shortcuts import render

# Create your views here.

from .forms import CharFieldExamples
from .models import User

def form_fields_examples(request): 
        if request.method == 'POST': 
                form = CharFieldExamples(request.POST)
                if form.is_valid(): 
                        name = form.cleaned_data['name']
                        roll = form.cleaned_data['roll']
                        email = form.cleaned_data['email']
                        agree =form.cleaned_data['agree']
                        print(agree)
                        user = User(name=name, roll=roll, email=email, agree=agree)
                        user.save()
                        
                        # for update 
                        # user = User(id=1, name=name, roll=roll, email=email, agree=agree)
                        # user.save()
                        
                        # # for delete 
                        # user = User(id=4)
                        # user.delete()
        else: 
                form = CharFieldExamples()
        return render(request, 'form_fields_app/home.html', {'form' : form})