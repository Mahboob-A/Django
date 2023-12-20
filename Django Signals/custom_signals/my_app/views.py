from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.cache import cache

from . import signals

# Create your views here.


def signup(request): 
        if not request.user.is_authenticated: 
                if request.method == 'POST': 
                        form = UserCreationForm(request.POST)
                        if form.is_valid(): 
                                print('in sign up form cleaned data : ', form.cleaned_data)
                                print('in sign up form: ', form)
                                print()
                                form.save()
                                messages.success(request, 'Log In Successful!')
                                return HttpResponseRedirect('/login/')
                else: 
                        form = UserCreationForm()        
                return render(request, 'my_app/signup.html', {'signup_form' : form})
        else: 
                return HttpResponseRedirect('/dashboard/')


def user_login(request): 
        if not request.user.is_authenticated: 
                if request.method == 'POST': 
                        form = AuthenticationForm(request=request, data=request.POST)
                        if form.is_valid(): 
                                username = form.cleaned_data['username']
                                password = form.cleaned_data['password']
                                user = authenticate(username=username, password=password)
                                if user is not None: 
                                        print('in login')
                                        print('user: ', user)
                                        print('un: ', username)
                                        print('pass: ', password)
                                        print()
                                        login(request=request, user=user)
                                        return HttpResponseRedirect('/dashboard/')
                else: 
                        form = AuthenticationForm()
                return render(request, 'my_app/login.html', {'login_form' : form})
        else: 
                return HttpResponseRedirect('/dashboard/')


def dashboard(request): 
        if request.user.is_authenticated: 
                print('in dashboard')
                messages.success(request, 'Log In Successful Dashboard!')
                user_ip = request.session.get('user_ip', None)
                username = request.user.username
                login_count = cache.get('login_count', 0, version=request.user.pk)
                
                # sending singal 
                # we can pass any kwargs in send method (key=value) and this will be received in the 
                # receiver function's kwargs. 
                signals.user_notification_signal.send(sender=request.user, request=request, username=request.user.username)
                
                return render(request, 'my_app/dashboard.html', {'username' : username, 'user_ip' : user_ip, 'login_count' : login_count})
        else: 
                return HttpResponseRedirect('/login/')
        
        

def user_logout(request): 
        logout(request)
        return HttpResponseRedirect('/login/')
        