

from django.contrib.auth.signals import user_logged_in
from django.dispatch import Signal, receiver
from django.core.cache import cache

from django.contrib.auth.models import User


# we just need to instantiate Signal class 
user_notification_signal = Signal()


@receiver(user_notification_signal)
def user_notification_signal_receiver(sender, request, **kwargs): # take these params | this signal is send from dashboard view | see the view 
        print()
        print('### user_notification_signal receiver ###')
        print('sender: ', sender)
        print('request: ', request)
        print(f'kwargs: , {kwargs}') 
        username = kwargs.get('username')
        print('username: ', username)
        print()

@receiver(user_logged_in, sender=User)
def login_count_receiver(sender, request, **kwargs):     
        print()
        print('### user logged in receiver ###')
        print('sender: ', sender)
        print(f'kwargs: , {kwargs}') 
        user = kwargs.get('user')
        # print('request.META: ', request.META) | request.META contains all the user's system information 
        
        # get user IP 
        ip = request.META.get('REMOTE_ADDR')
        request.session['user_ip'] =  ip
        
        # cache user log in count 
        login_count = cache.get('login_count', default=0, version=user.pk)
        cache.set('login_count', login_count + 1, version=user.pk)
        
        print()
        
