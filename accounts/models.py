from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserManager(BaseUserManager):
    """Manager for User"""

    def create_user(self, email, password, **kwargs):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email id')
        
        # makes email to lowercase 
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        
        # hashing the password
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        """Create and save a superuser"""
        user = self.create_user(email, password, **kwargs)

        user.is_superuser = True
        user.is_staff     = True
        user.save()

        return user
    


class User(AbstractBaseUser, PermissionsMixin):
    """ Model for  users """
    email           = models.EmailField(max_length=255, unique=True)
    firstname       = models.CharField(max_length=255)
    lastname        = models.CharField(max_length=255, blank=True)
    
    is_staff        = models.BooleanField(default=False) #sets django admin access to false

    objects = UserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['firstname']


    def __str__(self):
        """Return string representation of user"""
        return self.email


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Creates token when a new user is created"""
    if created:
        Token.objects.create(user=instance)
