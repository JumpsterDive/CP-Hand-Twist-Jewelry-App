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

def change_password(request):
    username = request.POST['username']
    new_password = request.POST['new_password']
    user = User.objects.get(username=username)
    user.set_password(new_password)
    user.save()
    return HttpResponse('User reset password')
#end def change_password



# Authentication, Login & Logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            userModeObject = User.objects.get(username=request.user)
            context = {'userInfo':userModelObject}

            return HttpResponse('user login successful')
        else:
            # Return to an 'invalid login' error message
            return HttpResponse("Login creditials did not match")
    return HttpResponse('Direct to Login page (home page?)')


def user_logout(request):
    logout(request)
    # redirect to a home page
    return HttpResponse('logout - redirect to homepage')
#end def user_logout


# Authorization



