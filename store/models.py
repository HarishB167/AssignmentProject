from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']
    
class SubCategory(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT) 
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']
    
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    subcategory = models.ForeignKey(
        SubCategory, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']
