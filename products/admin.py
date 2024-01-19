from django.contrib import admin
from .models import Category, Product, Color, Image
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(Image)