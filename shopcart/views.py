from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib import messages
from products.models import ProductItem
# from .forms import CartForm, CheckoutForm
from .cart import Shopcart
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.

def shopcart_summary(request):
    return render(request, 'shopcart/shoppingcart.html')

def shopcart_add(request):
    shopcart = Shopcart(request)    # save the session data
    if request.POST.get('action') == "post":
        product_id = int(request.POST.get('productid'))    # collect the productid from the data
        print(f'HERE {product_id}')
        product = get_object_or_404(ProductItem,id=product_id)   # find the object in the database 
        shopcart.add(product = product)   # Save the information to the session in the object class
        response = JsonResponse({'test':'data'})   # Send some Json data
        print(f'JSONPRINT {response}')
        return response




def checkout(request):
    # all_products = Product.objects.all()
    return render(request, "shopcart/checkout.html")



# def show_product(request, product_id):
#     if request.method == 'POST':
#         form = CartForm(request, request.POST)
#         if form.is_valid():
#             request.form_data = form.cleaned_data
#             cart.add_item_to_cart(request)
#             return redirect('show_cart')
        
#     form = CartForm(request, initial={'product_id':product.id})
#     return render(request, 'shopcart/shoppingcart.html', {
#                             'product': Product,
#                             'form': form,
#                             })