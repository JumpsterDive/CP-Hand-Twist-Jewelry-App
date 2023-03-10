from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def mainPageView(request):
    return render(request,'main_page/main_page.html')
#end def mainPageView

def aboutPageView(request):
    return render(request,'main_page/about.html')    
#end def aboutPageView

def contactPageView(request):
    return render(request, 'main_page/contact.html')
#end def contactPageView
