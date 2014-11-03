from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

from .forms import MyRegistrationForm

def login(request):
    
    token = {}
    token.update(csrf(request))
    return render_to_response('login.html', token)

def authenticate(request):
    
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
	auth.login(request, user)
	return HttpResponseRedirect('/login_success')
    else:
	return HttpResponseRedirect('/invalid')

def login_success(request):

    return render_to_response('login_success.html', {'first_name': request.user.username})

def invalid(request):

    return render_to_response('invalid.html')

def logout(request):

    auth.logout(request)
    return render_to_response('logout.html')

def register(request):

    if request.method == 'POST':
	form = MyRegistrationForm(request.POST)
	if form.is_valid():
	    form.save()
	    return HttpResponseRedirect('/register_success')
    else:
	form = MyRegistrationForm()

    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('register.html', token)

def register_success(request):

    return render_to_response('register_success.html')

