from django.db import models
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price=models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    category = models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True,related_name="products",)
    brand = models.CharField(max_length=100, blank=True, null=True)
    stock = models.PositiveBigIntegerField(default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    @property
    def savings(self):
        return self.original_price - self.discounted_price
    
    @property
    def discount_percentage(self):
        if self.original_price>0:
            return round(
                (self.savings / self.original_price) * Decimal("100")
            )
        return 0

    def __str__(self):
        return self.name


class Specification(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="specifications",
    )
    specification = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.product.name} - {self.specification}"
    
class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image=models.ImageField(upload_to="products/gallery/")
    def __str__(self):
        return f"{self.product.name}"
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="cart_items")
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.product.discounted_price * self.quantity
    def __str__(self):
        return f"{self.product.name} X {self.quantity}"