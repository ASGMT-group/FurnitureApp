from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager  # Assuming the manager is in the same app




class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    forget_password = models.CharField(max_length=100, null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    last_logout = models.DateTimeField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to="user_pic", height_field=None, width_field=None, max_length=None, default='user_pic/logo.png')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



     