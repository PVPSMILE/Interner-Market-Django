from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name_ru', 'name_ua', 'name_en')
    list_display_links = ('id', 'slug')

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'short_description', 'created_at')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title', 'short_description')
    list_filter = ('created_at',)
    