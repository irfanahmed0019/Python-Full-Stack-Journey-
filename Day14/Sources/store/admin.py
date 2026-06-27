from django.contrib import admin
from .models import (Product,Category,Specification,ProductImage,CartItem,)

# Register your models here.

class SpecificationInline(admin.TabularInline):
    model=Specification
    extra=1

class ProductImageInline(admin.TabularInline):
    model=ProductImage
    extra=1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[
        SpecificationInline,
        ProductImageInline
        ]

admin.site.register(Category)
admin.site.register(Specification)
admin.site.register(ProductImage)
admin.site.register(CartItem)