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

    print(total),

    # setup the intent which will then trigger respond a secret key
    stripe.api_key  = 'sk_test_51MpL6FG4DY3biWn460Tdt3qUUVqUorCebaQSFpfSyRZyRzQ5Dul0Zhz84vAo2RbeW9lr1ZUpdh0MJtU5wqAhHgzu00O1jKpM7L'
    intent = stripe.PaymentIntent.create(
        amount = total,
        currency='usd',
        metadata={'userid':request.user.id}
    )
    
    context = {'client_secret': intent.client_secret}

    return render(request, 'payment/payment_main.html',context) 