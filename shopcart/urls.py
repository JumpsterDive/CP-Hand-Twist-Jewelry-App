from django.urls import path
from . import views

app_name = 'shopcart'

urlpatterns = [
    path('checkout/', views.checkout, name ='checkout'),
    path('cart-summary/', views.shopcart_summary, name='shopcart_summary'),
    path('add/', views.shopcart_add, name='shopcart_add'), 
    path('delete/', views.shopcart_delete, name='shopcart_delete'), 
    path('update/', views.shopcart_update, name='shopcart_update'),
]