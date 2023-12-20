from django.shortcuts import render

# Create your views here.

from .forms import CharFieldExamples


def form_fields_examples(request): 
        if request.method == 'POST': 
                form = CharFieldExamples(request.POST)
                if form.is_valid(): 
                        print('From Is Validated')
                        print('Name: ',  form.cleaned_data['name'])
                        print('Roll: ',  form.cleaned_data['roll'])
                        print('Price: ',  form.cleaned_data['price'])
                        print('Agree: ',  form.cleaned_data['agree'])
                        print('Rate: ',  form.cleaned_data['rate'])
        else: 
                form = CharFieldExamples()
        return render(request, 'form_fields_app/home.html', {'form' : form})