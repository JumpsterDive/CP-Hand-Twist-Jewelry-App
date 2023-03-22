from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib import messages
# from .models import Product
# from .forms import CartForm, CheckoutForm


# Create your views here.

def shopcart_summary(request):
    return render(request, 'shopcart/shoppingcart.html')


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