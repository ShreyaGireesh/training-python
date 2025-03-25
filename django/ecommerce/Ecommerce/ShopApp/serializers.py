from rest_framework import serializers
from .models import Product, Category, CartItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__' 

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(read_only=True)
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True  # Allow multiple categories
    )

    class Meta:
        model = Product
        fields = ["id","name", "description", "price", "stock", "seller", "categories", "image"]
    def create(self, validated_data):
        categories = validated_data.pop("categories", [])  # Extract categories
        product = Product.objects.create(**validated_data)  # Create product
        product.categories.set(categories)  # Properly set categories
        return product

    def update(self, instance, validated_data):
        categories = validated_data.pop("categories", None)  # Extract categories if provided
        for attr, value in validated_data.items():
            setattr(instance, attr, value)  # Update product attributes
        instance.save()
        
        if categories is not None:
            instance.categories.set(categories)  # Use `.set()` for many-to-many update
            
        return instance

class CartItemSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(read_only=True)
    product_details = ProductSerializer(source="product", read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'customer', 'product', 'product_details', 'quantity', 'added_at']