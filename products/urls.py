from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('allproducts/', views.product_all, name ='product_all'),
    # path('productDetails/<int:id>/',views.productDetailsIndex, name='productDetailsIndex'),
    path('productDetail/<slug:slug>/', views.productDetail, name = 'productDetail'),
    path('search/<slug:category_slug>/',views.category_list , name='category_list')

]