
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



class ExampleMiddleware: 
        def __init__(self, fetch_respose) -> None:
                self.fetch_response = fetch_respose 
                print()
                print('Class Based Middleware __init__ ')
                print('this code will be executed ONLY ONCE when the server begins')
                print()
                
                
        def __call__(self, request):
                print()
                print('Class Based Middleware | Request  ')
                print('this code will be executed in each request / response cycle BEFORE the actual view is called/executed.')  # executed in request time 
                print()
                
                response = self.fetch_response(request)
                
                print()
                print('this code will be executed in each request/response cycle AFTER the actual view is called/executed.')  # executed in resposne time 
                print('Class Based Middleware | Response  ')
                print()
                
                return response 






                