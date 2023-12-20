
from django.shortcuts import render
from django.contrib.messages.middleware import MessageMiddleware

class SitesUnderConstructionMiddleware: 
        ''' Middleware to show site under construction for all requests '''
        
        def __init__(self, take_response) -> None:
                print('One Time Initialization of SitesUnderConstructionMiddleware Middleware Executed.')
                self.take_response = take_response
                
        
        def __call__(self, request): 
                print('Inside SitesUnderConstructionMiddleware - Request Cycle ')

                # we are rendering and returning that page only. so, no other view will be rendered.  
                response = render(request, 'my_app/sites_under_constructions.html')        
                
                print('Inside SitesUnderConstructionMiddleware - Response Cycle ')

                return response 

