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
 
    print(total)   #DEBUG

    # setup the intent which will then trigger respond a secret key
    '''
    Create a PaymentIntent on the server with an amount, currency.  Always decide how much to charge
    on the server side, a trusted environment as opposed to the client.  This prevents mailicious
    customers from being able to choose their own prices.

    Included in the return PaymentIntent is a client_secret, which teh client side uses to 
    securely complete the payment process instead of passing the entire PaymentIntent Object.   
    '''

    # Set your secret key. Remember to switch to your live secret key in production.
    # See your keys here: https://dashboard.stripe.com/apikeys

    stripe.api_key  = 'sk_test_51MpL6FG4DY3biWn460Tdt3qUUVqUorCebaQSFpfSyRZyRzQ5Dul0Zhz84vAo2RbeW9lr1ZUpdh0MJtU5wqAhHgzu00O1jKpM7L'
    intent = stripe.PaymentIntent.create(
        amount = total,
        currency='usd',
        metadata={'userid':request.user.id}
    )
    
    context = {'client_secret': intent.client_secret}

    return render(request, 'payment/payment_main.html',context) 