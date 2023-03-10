from django.urls import path, include
from . import views

app_name = 'main_page'

urlpatterns = [
    path('',views.mainPageView,name='mainPageView'),
    path('about/',views.aboutPageView,name='aboutPageView'),
    path('contact/',views.contactPageView,name='contactPageView'),
]