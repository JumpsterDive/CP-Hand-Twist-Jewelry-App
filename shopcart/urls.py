from django.urls import path
from . import views

app_name = 'shopcart'

urlpatterns = [
    path('checkout/', views.checkout, name ='checkout'),
]