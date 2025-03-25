from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, role="Customer", business_license=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, role=role)

        if role == "Seller":
            if not business_license:
                raise ValueError("Sellers must upload a business license")
            user.business_license = business_license
            user.is_active = False  # Seller needs admin approval

        else:
            user.is_active = True  # Customers are active by default

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user =self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.role = "Admin"
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ("Customer", "Customer"),
        ("Seller", "Seller"),
        ("Admin", "Admin")
    ]
    email = models.EmailField(unique = True)
    name = models.CharField(max_length = 255)
    role = models.CharField(max_length=10, choices = ROLE_CHOICES, default="Customer")
    business_license = models.FileField(upload_to="business_license/", null = True, blank = True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
