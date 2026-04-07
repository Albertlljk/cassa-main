from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] 
    prepopulated_fields = {'slug': ('name',)} 
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'is_popular'] 
    list_filter = ['category', 'available', 'is_popular']  
    list_editable = ['price', 'available', 'is_popular'] 
    prepopulated_fields = {'slug': ('name',)}  
admin.site.register(Product, ProductAdmin)
