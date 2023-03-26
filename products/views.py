from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import ProductItem 
from .models import Category
from .models import ProductType
from django.shortcuts import get_object_or_404
from django.views.generic import View


def product_all(request):
    all_products = ProductItem.products.all()
    return render(request, "products/products.html", {'all_products':all_products,})
#end def product_all

# Create your views here.
def categories(request):
    return{
        'categories':Category.objects.all()
    }

def category_list(request, category_slug=None):
    category = get_object_or_404(Category,slug=category_slug)
    products = ProductItem.objects.filter(category=category)
    return render(request, 'products/category.html', {'category': category, 'products': products})


def productIndexPage1(request,category_slug=None):

    products = ProductItem.products.all()

    print(category_slug)
    category = get_object_or_404(Category,slug=category_slug)

    print(products)

    # User.objects.get(username=request.user)
    # product = ProductItem.objects.get(product_type)
    # product = ProductItem(self.product_type)
    # print(product)
    # category = Category.objects.all()
    # product_types = ProductType.objects.get(id=id)
    # all_products = ProductItem.objects.filter(ProductItem.product_type)

    # all_products = ProductItem.objects.filter(product_type='Studs').first()
    # all_products = ProductItem.objects.filter().product_type('Cuffs')
    all_products = ProductType.objects.all()

    # queryset = ProductType.objects.all()
    # if self.request.GET.get('Cuffs'):
    #     queryset = queryset.filter(product_type=self.requessss.)


    print(all_products)
    # Cuffs
    # Studs
    # Gemstones
    # Ear Climbers
    

    # print(request)
    # print(category)
    # print(product_types)
    print(all_products)
    
    
    
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

def productDetailsIndex(request,id):
    # all_products = ProductItem.objects.all()
    # productDetailsObject = ProductItem.objects.filter(id=id)
    productDetailsObject = ProductItem.objects.get(id=id)
    context = {'productDetail': productDetailsObject}
    print(context)
    
    return render(request, "products/productDetails.html", context)

#end def productDetails_index


def productDetail(request,slug):

    product = get_object_or_404(ProductItem, slug=slug)
    # productDetailsObject = ProductItem.objects.get(id=id)
    # context = {'productDetail': productDetailsObject}
    context = {'productDetail': product}
    print(context)
    print("HERE")
    return render(request,'products/productsDetails.html',context)
    # all_products = ProductItem.objects.all()
    # productDetailsObject = ProductItem.objects.filter(id=id)
    # return render(request, "products/productDetails.html", context)
 

#end def productDetails_index