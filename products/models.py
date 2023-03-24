
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager,self).get_queryset().filter(is_active=True)


class Category(MPTTModel):
    """
    Category Table implemented with MPTT
    """
    
    name = models.CharField(verbose_name = ("Category Name"), help_text = ("Required and unique"),max_length = 255,unique = True)
    slug = models.SlugField(verbose_name = ("Category safe URL"),max_length=255,unique=True)
    parent = TreeForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="children")
    is_active = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    # def get_absolute_url(self):
    #     return reverse("store:category_list", args=[self.slug])
    
    def __str__(self):
        return self.name
#end class Category
    
class ProductType(models.Model):
    """
    ProductType table will provide a list of the different types of 
    products that are for sale
    """
    name = models.CharField(verbose_name = ("Product Name"),help_text = ("Required"),max_length = 255,unique = True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Product Type")
        verbose_name_plural = ("Product Types")

    def __str__(self):
        return self.name

#end class ProductType 

class ProductSpecification(models.Model):
    """
    The Product specification table contains product
    specification or features for the product types
    """
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField( verbose_name=("Name"), help_text=("Required"), max_length=255, blank =True)
    
    class Meta:
        verbose_name = ("Product specification")
        verbose_name_plural = ("Product Specifications")

    def __str__(self):
        return self.name
    
#end class ProductSpecification 
   

class ProductItem(models.Model):
    """
    The Product table containing all product items
    """
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    title = models.CharField(verbose_name=("title"), help_text=("Required"), max_length=255)
    description = models.TextField(verbose_name=("description"),help_text=("enter description of product"),blank=True)
    additional_description = models.TextField(verbose_name=("additional description"),help_text=("Not Required"),blank=True)
    slug = models.SlugField(max_length=255)
    regular_price= models.DecimalField(
        verbose_name=("Regular price"), 
        help_text=("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": ("The price must be between 0 and 999.99"),
            },
        },
        max_digits=5,
        decimal_places=2,
        )
    discount_price = models.DecimalField(
        verbose_name=("Discount price"),
        help_text=("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": ("The price must be between 0 and 999.99"),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(verbose_name=("Product visibility"),help_text=("Change product visibility"),default=True)
    created_at = models.DateTimeField(("Created at"), auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(("Updated at"), auto_now=True)
    objects = models.Manager()
    products = ProductManager()

    class Meta:
        ordering = ("created_at",)
        verbose_name = ("Product")
        verbose_name_plural = ("Products") 

    def __str__(self):
        return self.title
    
#end class ProductItem

class ProductSpecificationValue(models.Model):
    """
    The Product Specification value table holds each of the 
    products individual specification or features
    """
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification,on_delete=models.RESTRICT)
    value = models.CharField(verbose_name=("value"),help_text=("Product specification value (maximum of 255 words)"),max_length=255)

    class Meta:
        verbose_name = ("Product Specification Value")
        verbose_name_plural = ("Product Specification Values")

    def __str__(self):
        return self.value
    
#end class ProductSpecificationValue

    
class ProductImage(models.Model):
    """
    The Product Image Table
    """
    product = models.ForeignKey(ProductItem,default=None, on_delete=models.CASCADE, related_name="product_image")
    name = models.CharField(max_length=255)
    images = models.ImageField(
            verbose_name = ("image"),
            upload_to='product_images/', 
            help_text=("Upload a product image"),
            blank=True
            )
    alt_text = models.CharField(    
            help_text=("Please add alternative text"),
            max_length=255,
            null = True,
            blank = True
            )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Product Image")   # A human readable name for the object, singular
        verbose_name_plural = ("Product Images")  # a plural name for the object

#end class ProductImage
    


    

