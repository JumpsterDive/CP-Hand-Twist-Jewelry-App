from django.contrib import admin
from .models import ProductItem 
from .models import UploadImage
# from .models import ImageAlbum

# Register your models here.

class uploadImageAdmin(admin.StackedInline):
    model = UploadImage

@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    inlines = [uploadImageAdmin]

    class Meta:
        model = ProductItem

@admin.register(UploadImage)
class uploadImageAdmin(admin.ModelAdmin):
    pass


# admin.site.register(ProductItem)
# admin.site.register(UploadImage)
# admin.site.register(ImageAlbum)

