from django.urls import path
from . import views

app_name = 'shopcart'

urlpatterns = [
    path('checkout/', views.checkout, name ='checkout'),
    path('shoppingcart/', views.shopcart_summary, name='shopcart_summary'),
    path('add/', views.shopcart_add, name='shopcart_add') 
]