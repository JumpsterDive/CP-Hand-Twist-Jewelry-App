from django.urls import path, include
from . import views


app_name = 'users'

urlpatterns = [
    path('',views.usersIndex,name='usersIndex'),
    path('registration/',views.userRegistration, name = 'userRegistration'),
    path('userProfile/',views.userProfile, name='userProfile'),
    
]