from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom User Manager
class MyAccountManager(BaseUserManager):
    # Method to create a regular user
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")  # Email is required

        # Create a new user instance with provided details
        user = self.model(
            email=self.normalize_email(email),  # Normalize email (e.g., lowercase)
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)  # Hash the password before saving
        user.save(using=self._db)  # Save the user instance in the database
        return user

    # Method to create a superuser (admin user)
    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password  # Set password for the superuser
        )

        # Assign admin privileges
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using=self._db)  # Save the superuser instance
        return user

# Custom User Model
class Account(AbstractBaseUser):
    # Basic user details
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)  # Optional field

    # User activity and permissions
    date_joined = models.DateTimeField(auto_now_add=True)  # Set once when the user is created
    last_login = models.DateTimeField(auto_now=True)  # Updates every time the user logs in
    is_admin = models.BooleanField(default=False)  # Admin-level access
    is_staff = models.BooleanField(default=False)  # Staff permission for Django Admin
    is_active = models.BooleanField(default=False)  # Determines if the user can log in
    is_superadmin = models.BooleanField(default=False)  # Superuser privileges

    # User authentication fields
    USERNAME_FIELD = 'email'  # Use email as the unique identifier for login
    REQUIRED_FIELDS = ['first_name', 'last_name']  # No username required

    # Linking the custom manager to this model
    objects = MyAccountManager()

    # String representation of the user model
    def __str__(self):
        return self.email

    # User permissions handling
    def has_perm(self, perm, obj=None):
        return self.is_admin  # Admin users have all permissions

    def has_module_perms(self, app_label):
        return True  # Users can view the app in Django Admin
