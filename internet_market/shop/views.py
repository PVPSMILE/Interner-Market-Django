from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def shop_page(request):
    products = Product.objects.all()
    return render(request, 'shop/shop.html', context={'products': products})