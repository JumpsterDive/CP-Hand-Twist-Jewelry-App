from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect

# Create your views here.

def usersIndex(request):
    return HttpResponse('usersIndex OK')
#end def usersIndex


# Create and Edit users

def user_registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username,
                                        email,
                                        password,
                                        first_name=first_name,
                                        last_name=last_name)
        user.save()
        return HttpResponse('user registration saved')
    else:
        return HttpResponse('user registration Not Saved')
    
#end def user_registration

# Changing Passwords

# Authentication, Login & Logout

# Authorization



