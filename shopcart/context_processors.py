from .cart import Shopcart


def shopcart(request):
    return {'shopcart': Shopcart(request)}