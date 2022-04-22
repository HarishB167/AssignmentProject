from unicodedata import category
from rest_framework import serializers

from .models import Category, Product

    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'subcategory', 'subcategory_name','category']
        
    category = serializers.SerializerMethodField()
    subcategory_name = serializers.SerializerMethodField()
    
    def get_subcategory_name(self, product:Product):
        return str(product.subcategory)

    def get_category(self, product:Product):
        return product.subcategory.category.title
    
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'category']
        
    category = serializers.StringRelatedField()
