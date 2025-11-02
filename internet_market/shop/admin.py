# shop/admin.py
from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name_ua', 'name_ru', 'name_en')
    list_display_links = ('id', 'slug')
    search_fields = ('name_ua', 'name_ru', 'name_en')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'slug', 'created_at')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title', 'short_description')
    list_filter = ('created_at', 'category')

