from .models import CartItem, Product


class shopcart():
    '''
    A shopping cart class, providing some default behaviors that
    can be inherented or overrided, as necessary.
    '''



def cart_id(request):
    if 'cart_id' not in request.session:
        request.session['cart_id']= _generate_cart_id()

    return request.session['cart_id']

def generate_cart_id():
    pass


def get_all_cart_items(request):
    pass


def add_item_to_cart(request):
    pass

def item_count(request):
    pass


def subtotal(request):
    pass


def remove_item(request):
    pass

def update_item(request):
    pass

def clear(request):
    pass


