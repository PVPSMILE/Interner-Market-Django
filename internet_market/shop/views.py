from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def shop_page(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop/shop.html', context={'products': products, 'categories': categories})

def product_page(request, slug):
    
    product = Product.objects.get(slug=slug)
    
    return render(request, 'shop/product_detail.html', context={'product': product})
    