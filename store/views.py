from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Product, SubCategory
from .serializers import CategorySerializer, ProductSerializer, SubCategorySerializer


@api_view()
def product_list(request):
    queryset = Product.objects.all()
    subcategory_id = request.query_params.get('subcategory_id')
    if subcategory_id is not None:
        queryset = queryset.filter(subcategory_id=subcategory_id)
    category_id = request.query_params.get('category_id')
    if category_id is not None:
        queryset = queryset.filter(subcategory_id__category_id=category_id)
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def product_detail(request, id):    
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def categories_list(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def category_detail(request, id):
    category = get_object_or_404(Category, pk=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view()
def subcategories_list(request):
    queryset = SubCategory.objects.all()
    category_id = request.query_params.get('category_id')
    if category_id is not None:
        queryset = queryset.filter(category_id=category_id)
    serializer = SubCategorySerializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def subcategory_detail(request, id):
    category = get_object_or_404(SubCategory, pk=id)
    serializer = SubCategorySerializer(category)
    return Response(serializer.data)