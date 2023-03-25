from django.shortcuts import render
from django.http import HttpResponse
from products.models import ProductItem
from .cart import Shopcart
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.

def shopcart_summary(request):
    shopcart = Shopcart(request)  # intiatiate an object class
    context = {'shopcart':shopcart}
    print(f'ShoppingCart_summary: {shopcart}')
    return render(request, 'shopcart/shoppingCartSummary.html',context)

def shopcart_add(request):
    shopcart = Shopcart(request)    # save the session data
    if request.POST.get('action') == "post":
        product_id = int(request.POST.get('productid'))    # collect the productid from the java query
        product_qty = int(request.POST.get('productqty'))    # collect the product qty from the java query
        product = get_object_or_404(ProductItem,id=product_id)   # find the object in the database 
        shopcart.add(product = product, product_qty=product_qty)   # Save the information to the session in the object class

        shopcartqty = shopcart.__len__()
        # shopcart_item_total = shopcart.__iter__()
        
        # print(f'Itemtotal {shopcart_item_total}')
        response = JsonResponse({'qty':shopcartqty})   # Send some Json data this will show all the updated items based upon what is in the basket
        return response

def shopcart_delete(request):
    shopcart = Shopcart(request)    # save the session data
    if request.POST.get('action') == "post":        
        product_id = int(request.POST.get('productid'))    # collect the productid from the java quer
        shopcart.delete(product = product_id)   # Send the information to the session in the object class for deletion
        shopcart_qty = shopcart.__len__()
        shopcart_total = shopcart.get_total_price()
        response = JsonResponse({'qty': shopcart_qty, 'subtotal': shopcart_total})
        return response
    
def shopcart_update(request):
    shopcart = Shopcart(request)    # save the session data
    if request.POST.get('action') == "post":        
        product_id = int(request.POST.get('productid'))    # collect the productid from the java query
        product_qty = int(request.POST.get('productqty'))
        shopcart.update(product=product_id, qty=product_qty)

        shopcart_qty = shopcart.__len__()
        shopcart_total = shopcart.get_total_price()
        # shopcart_item_total = shopcart.__iter__()
        # print(f'Itemtotal {shopcart_item_total}')
        
        response = JsonResponse({'qty': shopcart_qty, 'subtotal': shopcart_total,'item_qty': product_qty})
        return response


def checkout(request):
    shopcart = Shopcart(request)  # intiatiate an object class
    context = {'shopcart':shopcart}
    # all_products = Product.objects.all()
    return render(request, "shopcart/checkout.html",context)



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