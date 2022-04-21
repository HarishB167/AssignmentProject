from django.contrib import admin
from . import models

admin.site.register(models.Category)

@admin.register(models.SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    ordering = ['title', 'category']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'subcategory']
    ordering = ['title', 'subcategory']
