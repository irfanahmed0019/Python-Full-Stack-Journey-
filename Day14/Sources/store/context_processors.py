from .models import CartItem

def cart_count(request):
    cart_items=CartItem.objects.all()
    count=sum(item.quantity for item in cart_items)

    return{"cart_count":count,}