from rest_framework import permissions

class IsSellerOrAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # Allow GET (view) requests for everyone
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True
        
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in ["POST"]:  # Adding products
            return request.user.role == "Seller" and request.user.is_active

        # Allow only authenticated users
        return True
    
    def has_object_permission(self, request, view, obj):
        # Allow GET (view) requests for everyone
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Admins can do anything
        if request.user.role == "Admin":
            return True

        # Check if user is the product owner (seller) and is active
        return obj.seller == request.user and request.user.is_active

class IsAdminOnly(permissions.BasePermission):
    """
    Custom permission to allow only Admins to add/edit/delete categories.
    Everyone can view categories.
    """

    def has_permission(self, request, view):
        # Allow GET requests for everyone (View categories)
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Allow only admins to add/edit/delete categories
        return request.user.is_authenticated and request.user.role == "Admin"

class IsCustomer(permissions.BasePermission):
    """Permission to allow only customers (non-staff users) to access cart."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_staff