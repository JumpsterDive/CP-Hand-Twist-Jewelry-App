from django.db import models

# Create your models here.

# class ImageAlbum(models.Model):
#     def default(self):
#             return self.images.filter(default=True).first()
        
#     def thumbnails(self):
#             return self.images.filter(width__lt=100,length_lt=100)

#end class ImageAlbum
    




class ProductItem(models.Model):
    CATEGORY = [
        ('Earrings','Earrings'),
        ('EarClimbers','EarClimbers')
    ]
    TYPE = [
        ('Studs','Studs'),
        ('Cuffs','Cuffs'),
        ('Gemstone','Gemstone'),
    ]
    STYLE = [
        ('basic','basic'),
        ('fancy','fancy'),
    ]
    COLOR = [
        ('silver','silver'),
        ('gold','gold'),
    ]
    SIZE = [
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
    ]
    name = models.CharField(max_length=191)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    image = models.FileField(blank=True)
    # album = models.OneToOneField(ImageAlbum,related_name='model',on_delete=models.CASCADE, default=None)
    category = models.CharField(max_length=191, blank=True, choices=CATEGORY)
    type = models.CharField(max_length=191, blank =True, choices=TYPE)
    style = models.CharField(max_length=191, blank =True, choices=STYLE)
    color = models.CharField(max_length=191, blank =True, choices=COLOR)
    size = models.CharField(max_length=191, blank =True, choices=SIZE)

    def __str__(self):
        return f'{self.name} {self.price} {self.description} {self.image} {self.category} {self.style} {self.color} {self.size}'
    
#end class ProductItem
    
class UploadImage(models.Model):
    name = models.CharField(max_length=255)
    images = models.ImageField(upload_to='product_images/', blank=True)
    default = models.BooleanField(default=False)
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(ProductItem,default=None, on_delete=models.CASCADE, related_name="product_image")
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

#end class UploadImage
    


    

