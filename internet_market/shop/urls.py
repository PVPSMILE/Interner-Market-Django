from django.urls import path
from .views import *

urlpatterns = [
    path('shop/', shop_page, name='shop_page_link'),
    path('shop/<slug:slug>/', product_page, name='product_detail')
    
]
