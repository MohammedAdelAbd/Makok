from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=100, unique=True, blank=False)
    price = models.FloatField(blank=True)
    descriptions = models.TextField( blank=True )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image_url = models.URLField()
    file_id = models.TextField()
    
    def __str__(self):
        return f"{self.product.name} Image"
     
class Customers(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    university = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    batch_number = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name
    
class Orders(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    position = models.CharField(max_length=50, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)
    design_image = models.URLField(null=True, blank=True)
    logo_image = models.URLField(null=True, blank=True)
    color_image = models.URLField(null=True, blank=True)