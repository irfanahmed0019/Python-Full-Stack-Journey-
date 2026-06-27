from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:id>/", views.product, name="product"),
    path("cart/", views.cart, name="cart"),
    path("review/", views.review, name="review"),
    path("shipping/", views.shipping, name="shipping"),
    path("order/", views.order, name="order"),
    path("payment/", views.payment, name="payment"),
    path("confirmed/", views.confirmed, name="confirmed"),
    
    path("add-to-cart/<int:id>/",views.add_to_cart, name="add_to_cart"),
    path("cart/increase/<int:id>/",views.increase_quantity,name="increase_quantity"),
    path("cart/decrease/<int:id>/",views.decrease_quantity,name="decrease_quantity"),
    path("cart/delete/<int:id>",views.delete_cart_item,name="delete_cart_item"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)