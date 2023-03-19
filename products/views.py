from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import ProductItem

# Create your views here.


def productIndexPage1(request):
    all_products = ProductItem.objects.all()
    return render(request, "products/products.html", {
                                    'all_products':all_products,
                                     })

def productPage2_index(request):
    all_products = ProductItem.objects.all()
    return render(request, "products/products.html", {
                                    'all_products':all_products,
                                     })

def productPage3_index(request):
    all_products = ProductItem.objects.all()
    return render(request, "products/products.html", {
                                    'all_products':all_products,
                                     })

def productDetailsIndex(request):
    all_products = ProductItem.objects.all()
    # productDetailsObject = ProductItem.objects.filter(id=id)
    # context = {'productDetail': productDetailsObject}
    return render(request, "products/productDetails.html", {
                                    'all_products':all_products,
                                     })
 

#end def productDetails_index