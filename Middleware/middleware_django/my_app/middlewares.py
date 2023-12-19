
from django.shortcuts import HttpResponse 
# Function Based Middleware 

def example_middleware(get_response):  # the name of the param is not strict 
        print()
        print('Function Based Middleware | Outer Func ')
        print('this code will be executed ONLY ONCE when the server begins')
        print()
        
        def example_function(request): 
                print()
                print('Function Based Middleware  | Request ')
                print('this code will be executed in each request / response cycle BEFORE the actual view is called/executed.')  # executed in request time 
                print()
                
                response = get_response(request)
                
                print()
                print('this code will be executed in each request/response cycle AFTER the actual view is called/executed.')  # executed in resposne time 
                print('Function Based Middleware  |  Response  ')
                print()
                
                return response
        return example_function 



''' process_view hook middleware '''

class ExampleProcessViewMiddleware: 
        ''' 
        Middleware with process_view hook. 
        '''
        def __init__(self, fetch_respose) -> None:
                self.fetch_response = fetch_respose 
                print()
                print('ExampleProcessViewMiddleware Middleware __init__ ')
                print('this code will be executed ONLY ONCE when the server begins')
                print()
                
                
        def __call__(self, request):
                a = 10 
                b = 20 
                c = b + a 
                print('sum: ', c)
                print()
                print('ExampleProcessViewMiddleware Middleware | Request  ')
                print('this code will be executed in each request / response cycle BEFORE the actual view is called/executed.')  # executed in request time 
                print()
                
                response = self.fetch_response(request)
                
                print()
                print('this code will be executed in each request / response cycle AFTER the actual view is called/executed.')  # executed in resposne time 
                print('ExampleProcessViewMiddleware Middleware | Response  ')
                print()
                
                return response 

        ''' HOOKS (we can define more than one hook in same middleware.) '''
        
        '''
        the above code of this line: response = self.fetch_response(request) (in __call__) will be executed first and then this process_view
        hook will be executed. 
        '''
        # process view is is a hook, and this gets executed before view is executed. 
        def process_view(middleware, request, func, *args, **kwargs): # middleware, request and actual view function is passed *args. 
                print()
                print('this is process view hook. it is run before the actual view')
                print('middleware: ', middleware)
                print('request: ', request)
                print('args: ', args)
                print(f'kwargs: {kwargs}')
                print('func: ', func)
                print('Inside Process View ')
                # return HttpResponse('As process view returned HttpResponse, No View will be executed.')
                return None  # if None is returned, view will be executd. 
                
        # process exception hook to process exception 
        '''
        the below code of this line : response = self.fetch_response(request) (in __call__) will be executed after process_exception hook.  
        process_exception hook will only be triggered only if the view has exception. 
        '''
        '''
        def process_exception(self, request, exception): 
                # exception_class = exception.__class_.__name__
                print('this is process exception hook. it is run after the actual view is executed. ')
                print('request: ', request)
                print('exception: ', exception)
                # print('exception class name : ', exception_class)
                
                exception = f'An Error Occurred : {exception}'
                
                # if we return HttpResponse, we will see the error and not actual error page of Django. 
                return HttpResponse(exception)
                
                # if we return None, we will see the actual error page of Django 
                # return None 
        '''
           
                 
''' process_exception hook middleware '''
                
class ExampleProcessExceptionMiddleware: 
        ''' 
        Middleware with process_exception hook. 
        '''
        def __init__(self, fetch_respose) -> None:
                self.fetch_response = fetch_respose 
                print()
                print('ExampleProcessExceptionMiddleware Middleware __init__ ')
                print('this code will be executed ONLY ONCE when the server begins')
                print()
                
                
        def __call__(self, request):
                print()
                print('ExampleProcessExceptionMiddleware Middleware | Request  ')
                print('this code will be executed in each request / response cycle BEFORE the actual view is called/executed.')  # executed in request time 
                print()
                
                response = self.fetch_response(request)
                
                print()
                print('this code will be executed in each request / response cycle AFTER the actual view is called/executed.')  # executed in resposne time 
                print('ExampleProcessExceptionMiddleware Middleware | Response  ')
                print()
                
                return response 

        ''' HOOKS '''
           
        # process exception hook to process exception 
        '''
        the below code of this line : response = self.fetch_response(request) (in __call__) will be executed after process_exception hook.  
        process_exception hook will only be triggered only if the view has exception. 
        '''
        def process_exception(self, request, exception): 
                # exception_class = exception.__class_.__name__
                print('this is process exception hook. it is run after the actual view is executed. ')
                print('request: ', request)
                print('exception: ', exception)
                # print('exception class name : ', exception_class)
                
                exception = f'An Error Occurred : {exception}'
                
                # if we return HttpResponse, we will see the error and not actual error page of Django. 
                return HttpResponse(exception)
                
                # if we return None, we will see the actual error page of Django 
                # return None 
                
                

''' process_template_response hook middleware '''
                
class ExampleProcessTemplateResponseMiddleware: 
        ''' 
        Middleware with process_template_response hook. 
        '''
        def __init__(self, fetch_respose) -> None:
                self.fetch_response = fetch_respose 
                print()
                print('ExampleProcessTemplateResponseMiddleware Middleware __init__ ')
                print('this code will be executed ONLY ONCE when the server begins')
                print()
                
                
        def __call__(self, request):
                print()
                print('ExampleProcessTemplateResponseMiddleware Middleware | Request  ')
                print('this code will be executed in each request / response cycle BEFORE the actual view is called/executed.')  # executed in request time 
                print()
                
                response = self.fetch_response(request)
                
                print()
                print('this code will be executed in each request / response cycle AFTER the actual view is called/executed.')  # executed in resposne time 
                print('ExampleProcessTemplateResponseMiddleware Middleware | Response  ')
                print()
                
                return response 

        ''' HOOKS '''
           
        # process exception hook to process exception 
        '''
        the below code of this line : response = self.fetch_response(request) (in __call__) will be executed after process_template_response hook.  
        '''
        def process_template_response(self, request, response): 
                print()
                print('This is process_template_response hook ')
                print('request: ', request)
                print('response: ', response)
                print()
                response.context_data['sub'] = 'CSE'  # can change context data 
                response.context_data['status'] = 'Good'  # can add context data 
                response.template_name = 'my_app/template_resp_2.html' # can change which template file to render 
                return response 



