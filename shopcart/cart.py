from decimal import Decimal
from products.models import ProductItem


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

    def add(self,product,product_qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)   # Save the product ID

        if product_id in self.shoppingcart:
            self.shoppingcart[product_id]['qty'] = product_qty
        else: 
            self.shoppingcart[product_id]={'price':str(product.regular_price),'qty':int(product_qty)}

        # if product_id not in self.shoppingcart:    # If the product Id is not in the basket the create an item in the basket
        #     self.shoppingcart[product_id] = {'price':str(product.regular_price),'qty':int(product_qty)}

        self.save()  # Tell Django to save the sessions
 

    def __len__(self):
        '''
        Get the basket data and count the qty of items
        '''
        return sum(item['qty'] for item in self.shoppingcart.values())  # for each value in the product sum of all the values calculated 
    
    
    def __iter__(self):      
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.shoppingcart.keys()   # collect all the keys of the product id within the session data
        products = ProductItem.products.filter(id__in=product_ids)
        shoppingcart = self.shoppingcart.copy()   # make a copy of the session data

        for product in products:     # iterate over the products 
            shoppingcart[str(product.id)]['product']= product

        for item in shoppingcart.values():   # select individual values
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']  
            yield item

    
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['qty'] for item in self.shoppingcart.values())
    
    def delete(self,product):
        '''
        Delete item from session data
        '''
        product_id = str(product)   # assign the product id
        if product_id in self.shoppingcart:     # find in the product id in the basket
            del self.shoppingcart[product_id]
        self.save()   
    
    #end def delete

    def update(self, product, qty):
        '''
        Update values in session data from the shopping cart
        '''
        product_id = str(product)
        product_qty = qty

        if product_id in self.shoppingcart:
            self.shoppingcart[product_id]['qty'] = product_qty
        self.save()




    def save(self):
        self.session.modified=True


    


#end class Shopcart
