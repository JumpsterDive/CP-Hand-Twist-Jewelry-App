from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('productsPage1/', views.productIndexPage1, name ='productIndexPage1'),
    path('productDetails/',views.productDetailsIndex, name='productDetailsIndex'),
]