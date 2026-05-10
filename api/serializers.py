from rest_framework import serializers
from .models import *

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image_url','file_id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)   
    category = CategorySerializer(read_only=True)
     
    category_id = serializers.PrimaryKeyRelatedField(
        source='category', queryset=Category.objects.all(), write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'descriptions', 'category', 'category_id','images']
    def create(self, validated_data):
        images_data = validated_data.pop('images')
        product = Product.objects.create(**validated_data)

        for image in images_data:
            ProductImage.objects.create(product=product, **image)

        return product

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'position', 'text','design_image', 'logo_image', 'color_image']
        
class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    items = OrderItemSerializer(many=True, required=False)

    class Meta:
        model = Orders
        fields = ['id', 'customer', 'items', 'created_at']

    def create(self, validated_data):
        customer_data = validated_data.pop('customer')
        items_data = validated_data.pop('items')

        # إنشاء الزبون
        customer = Customers.objects.create(**customer_data)

        # إنشاء الطلب
        order = Orders.objects.create(customer=customer)

        # إنشاء العناصر (Order Items)
        for item in items_data:
            OrderItem.objects.create(order=order, **item)

        return order





