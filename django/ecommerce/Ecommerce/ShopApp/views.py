from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Category, Product, CartItem
from .serializers import CategorySerializer, ProductSerializer, CartItemSerializer
from .permissions import IsSellerOrAdmin, IsAdminOnly, IsCustomer
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    - Sellers can add, edit, and delete their own products.
    - Customers can only view products.
    - Admins have full access.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsSellerOrAdmin] 
    parser_classes = [MultiPartParser, FormParser] 

    def perform_create(self, serializer):
        """Set the seller field to the logged-in user when adding a product."""
        serializer.save(seller=self.request.user)
    
    def update(self, request, *args, **kwargs):
        """Allow only the seller who created the product to edit it."""
        product = self.get_object()
        if request.user != product.seller and not request.user.is_superuser:
            return Response({"error": "You can only edit your own products."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """Allow only the seller who created the product to delete it."""
        product = self.get_object()
        if request.user != product.seller and not request.user.is_superuser:
            return Response({"error": "You can only delete your own products."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retrieve all products",
        responses={200: ProductSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new product (only sellers & admins)",
        request_body=ProductSerializer,
        responses={201: ProductSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Update an existing product (only the seller or admin)",
        request_body=ProductSerializer,
        responses={200: ProductSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a product (only the seller or admin)",
        responses={204: "Product deleted successfully"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing categories.
    - Everyone can view (GET).
    - Only Admins can add, edit, delete.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOnly] 

    @swagger_auto_schema(
        operation_description="Retrieve a list of all categories.",
        responses={200: CategorySerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new category (Admin only).",
        request_body=CategorySerializer,
        responses={201: CategorySerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Retrieve details of a single category.",
        responses={200: CategorySerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a category (Admin only).",
        request_body=CategorySerializer,
        responses={200: CategorySerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a category (Admin only).",
        responses={204: "Category deleted successfully"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CartItemViewSet(viewsets.ModelViewSet):
    """ViewSet for handling cart operations"""
    serializer_class = CartItemSerializer
    permission_classes = [IsCustomer]

    def get_queryset(self):
        """Get only the cart items belonging to the logged-in user"""
        if getattr(self, 'swagger_fake_view', False):  # Check if it's Swagger schema generation
            return CartItem.objects.none()  # Return an empty queryset to avoid errors
        return CartItem.objects.filter(customer=self.request.user)

    @swagger_auto_schema(
        operation_description="Retrieve the cart items for the logged-in user.",
        responses={200: CartItemSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        """List all cart items of the authenticated user"""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Add a product to the cart (only for customers).",
        request_body=CartItemSerializer,
        responses={201: CartItemSerializer, 400: "Bad Request"}
    )
    def create(self, request, *args, **kwargs):
        """Ensure only customers can add products to their cart"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        user = request.user

        cart_item, created = CartItem.objects.get_or_create(customer=user, product=product)
        if not created:
            cart_item.quantity += quantity  # Increase quantity if already exists
        else:
            cart_item.quantity = quantity  # Otherwise, set new quantity

        cart_item.save()
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description="Update quantity of a cart item.",
        request_body=CartItemSerializer,
        responses={200: CartItemSerializer, 400: "Bad Request"}
    )
    def update(self, request, *args, **kwargs):
        """Update the quantity of a cart item"""
        instance = self.get_object()
        if instance.customer != request.user:  # Check if the logged-in user is the owner
            return Response({"error": "You can only update your own cart items."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Remove an item from the cart.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        """Remove an item from the cart"""
        instance = self.get_object()
        if instance.customer != request.user:  # Check if the logged-in user is the owner
            return Response({"error": "You can only delete your own cart items."}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)