"""CP_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


# add URL maps to redirect the base URL to our application
# Use static() to add URL mapping to serve static files during development (only)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('shopcart/',include('shopcart.urls',namespace='shopcart')),
    path('products/',include('products.urls')),
    path('main_page/',include('main_page.urls')),
    path('payment/',include('payment.urls')),
    path('accounts/',include("django.contrib.auth.urls")),  # Add Django site authentication urls (for login, logout, password management)
    # path('accounts/', include('allauth.urls')),  
    path('', RedirectView.as_view(url='main_page/',permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

'''
Note that you do not necessarily need the URLs provided by django.contrib.auth.urls. 
Instead of the URLs login, logout, and password_change (among others), 
you can use the URLs provided by allauth: account_login, account_logout, 
account_set_password…
'''