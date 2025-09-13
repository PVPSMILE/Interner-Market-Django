from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField((""))
    name_ru = models.CharField(max_length=100)
    name_ua = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    
# class Color:
#     name = models.CharField(50)
#     hex_color = models.CharField(7 , default="#00000")

    def __str__(self):
        return self.name
    


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.TextField()
    long_description = models.TextField()
    # palitre = models.ManyToManyField(Color, blank=True, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title