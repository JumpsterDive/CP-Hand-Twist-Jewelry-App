from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    ProductItem,
    ProductImage,
    ProductSpecification,
    ProductType,
    ProductSpecificationValue
)

admin.site.register(Category,MPTTModelAdmin)

class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        ProductSpecificationInline,
    ]

class ProductImageInline(admin.TabularInline):
    model = ProductImage

class ProductSpeficationValueInline(admin.TabularInline):
    model = ProductSpecificationValue

@admin.register(ProductItem)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ProductSpeficationValueInline,
    ]






# # Register your models here.

# class ProductImageAdmin(admin.StackedInline):
#     model = ProductImage

# @admin.register(ProductItem)
# class ProductItemAdmin(admin.ModelAdmin):
#     inlines = [ProductImageAdmin]

#     class Meta:
#         model = ProductItem

# @admin.register(UploadImage)
# class uploadImageAdmin(admin.ModelAdmin):
#     pass


# # admin.site.register(ProductItem)
# # admin.site.register(UploadImage)
# # admin.site.register(ImageAlbum)

