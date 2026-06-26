from django.shortcuts import render


def home(request):
    return render(request,"home.html")

def product(request):
    return render(request,"product.html")

def cart(request):
    return render(request,"cart.html")

def review(request):
    return render(request,"review.html")

def shipping(request):
    return render(request,"shipping.html")

def order(request):
    return render(request,"order.html")

def payment(request):
    return render(request,"payment.html")

def confirmed(request):
    return render(request, "confirmed.html")