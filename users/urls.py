from django.urls import path, include
from . import views
# from users.views import userProfile



app_name = 'users'

urlpatterns = [
    path('',views.usersIndex,name='usersIndex'),
    path('accounts/',include("django.contrib.auth.urls"))
]