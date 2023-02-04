from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra):
        if not email:
            raise ValueError(_("Email should be provided"))

        email = self.normalize_email(email)
        new_user = self.model(email=email, **extra)
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user


    def create_superuser(self, email, password, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)
        extra.setdefault('is_active', True)

        if extra.get('is_staff') is not True:
            raise ValueError(_("Superuser access denied"))
        if extra.get('is_superuser') is not True:
            raise ValueError(_("Superuser access denied"))
        if extra.get('is_active') is not True:
            raise ValueError(_("Superuser access denied"))
        return self.create_user(email, password, **extra)


class User(AbstractUser):
    # user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=25, unique = True)
    email = models.EmailField(max_length=80, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True)
    password = models.CharField(null=False, max_length=255)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email', 'phone_number', 'password']

    objects=CustomUserManager()

    # def __str__(self):
    #     return f"User: {self.email}"