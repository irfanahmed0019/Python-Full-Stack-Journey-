from django.shortcuts import render, get_object_or_404,redirect
from .models import Product,CartItem


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def product(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "product.html", {"product": product})


def cart(request):
    cart_items=CartItem.objects.all()
    total=sum(item.total_price for item in cart_items)
    context={
        "cart_items":cart_items,
        "total":total,
    }
    return render(request, "cart.html",context)


def review(request):
    return render(request, "review.html")


def shipping(request):
    return render(request, "shipping.html")


def order(request):
    return render(request, "order.html")


def payment(request):
    return render(request, "payment.html")


def confirmed(request):
    return render(request, "confirmed.html")


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_item, created = CartItem.objects.get_or_create(
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")

def increase_quantity(request,id):
    cart_item=get_object_or_404(CartItem,id=id)

    cart_item.quantity+=1
    cart_item.save()
    return redirect("cart")

def decrease_quantity(request,id):
    cart_item=get_object_or_404(CartItem,id=id)

    if cart_item.quantity > 1:
        cart_item.quantity-=1
        cart_item.save()
    
    else:
        cart_item.delete()
    return redirect("cart")
 
def delete_cart_item(request,id):
    cart_item=get_object_or_404(CartItem,id=id)
    cart_item.delete()
    return redirect("cart")