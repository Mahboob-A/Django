from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse 

# Create your views here.

# for process_view hook 
def example_view(request): 
        print()
        print('example view is executed')
        print()
        return HttpResponse('this is example view response')

# for process_exception hook 
def example_view2(request): 
        # a = 1 / 0 
        print()
        print('example view 2 is executed')
        # a = 1 / 0 
        raise ValueError('value error raised')
        print()
        # return HttpResponse('this is example view2 response')


# for process_template_respone hook 

def process_template_response_hook_view(request): 
        print()
        print('executed view : process_template_response_hook_view')
        context = {'name' : 'Mahboob Alam', 'sub' : 'Eng'}
        a = 1 / 0 
        return TemplateResponse(request, 'my_app/template_response.html', context=context)
