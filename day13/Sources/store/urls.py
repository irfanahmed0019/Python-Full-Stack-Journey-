from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("product/",views.product,name="product"),
    path("cart/",views.cart,name="cart"),
    path("review/",views.review,name="review"),
    path("shipping/",views.shipping,name="shipping"),
    path("order/",views.order,name="order"),
    path("payment/",views.payment,name="payment"),
    path("confirmed/",views.confirmed,name="confirmed"),
]