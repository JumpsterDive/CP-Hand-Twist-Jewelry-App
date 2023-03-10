from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views import View
from django import forms
from django.views.generic import ListView
from django.urls import reverse


from users.forms import userRegistrationForm

# Create your views here.

# class userProfile_FormView(View):
#     model = userProfile_FormView


@login_required
def usersIndex(request):
    # return HttpResponse('usersIndex OK')
    return render(request,'main_page/main_page.html')
#end def usersIndex



# Create and Edit users

def userRegistration(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request(binding):
        form = userRegistrationForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['firstName']
            last_name = form.cleaned_data['lastName']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = User.objects.create_user(username,
                                            email,
                                            password,
                                            first_name=first_name,
                                            last_name=last_name)
            user.save()            
            # redirect to a new URL
            return HttpResponseRedirect(reverse('users:usersIndex'))
            # return HttpResponse('user registration saved')        
        else:
            return HttpResponse('user registration Not Saved')
    # If this is a GET (or any other method) create the default form.
    else:
        form = userRegistrationForm()

    context = {
        'form':form
    }

    return render(request,'registration/registration_form.html',context)

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

def user_authentication(request):
    if request.user.is_authenticated:
        return HttpResponse("User Authenticated")
    else:
        return HttpResponse('You must be logged in to see this view')


# Authorization



