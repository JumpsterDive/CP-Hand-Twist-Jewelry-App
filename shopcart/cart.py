# from .models import CartItem, Product


class Shopcart():
    '''
    A shopping cart class, providing some default behaviors that
    can be inherented or overrided, as necessary.
    '''
    def __init__(self,request):
        self.session = request.session
        shoppingcart = self.session.get('skey') 
        if 'skey' not in request.session:
            shoppingcart = self.session['skey'] = {}
        self.shoppingcart = shoppingcart

    def add(self,product):
        """
        Adding and updating the users basket session data
        """
        product_id = product.id   # Save the product ID
        print(f'product_id: {product.regular_price}')

        if product_id not in self.shoppingcart:    # If the product Id is not in the basket the create an item in the basket
            self.shoppingcart[product_id] = {'price':str(product.regular_price)}

        self.session.modified = True   # Tell Django to save the sessions

# def cart_id(request):
#     if 'cart_id' not in request.session:
#         request.session['cart_id']= _generate_cart_id()

#     return request.session['cart_id']

# def generate_cart_id():
#     pass


# def get_all_cart_items(request):
#     pass


# def add_item_to_cart(request):
#     pass

# def item_count(request):
#     pass


# def subtotal(request):
#     pass


# def remove_item(request):
#     pass

# def update_item(request):
#     pass

# def clear(request):
#     pass


