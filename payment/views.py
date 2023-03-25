import json
import stripe

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from shopcart.cart import Shopcart

# Create your views here.

@login_required
def shoppingCartView(request):

    # Get all the user information from the session and establish elements for sending the intent
    shoppingcart = Shopcart(request)
    total = str(shoppingcart.get_total_price())   # Get the total price  
    #(Stripe requires an integer convert to string then remove the decimal and then type set as integer
    total = total.replace('.','')
    total = int(total)

    stripe.api_key  = 'pk_test_51MpL6FG4DY3biWn4lJxPf1gsnBTTaJVU0f6FOuLHP3F0jPR33WIOx6twS5VKy9W3J0vBOr4y2GhnpAo6neaKGzFy000oIcOu1d'
    intent = stripe.PaymentIntent.create(
        amount = total,
        currency='usa',
        metadata={'userid':request.user.id}
    )
    

    return render(request, 'payment/payment_main.html') 