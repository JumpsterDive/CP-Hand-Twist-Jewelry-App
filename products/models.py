from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=191)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', blank=True)

    def __str__(self):
        return f'{self.name} {self.price} {self.description} {self.image}'
    


    

