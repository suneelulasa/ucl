from django.db import models

# Create your models here.
from threading import local

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

_thread_local = local()


class UserManager(BaseUserManager):
    """
    Implementation hints from *Practical Django and Channels*
    See https://www.amazon.com/s?k=practical+dango+2+and+channels+2
    """
    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        if extra_field.get('is_staff') is not True:
            raise ValueError("superuser must be staff")
        if extra_field.get('is_superuser') is not True:
            raise ValueError('superuser must be superuser (obviously!)')
        return self._create_user(email, password, **extra_field)


class User(AbstractUser):

    class Meta:
        permissions = [
            ("view_all_user", "Can view all users")
        ]

    username = None
    email = models.EmailField('email_address', unique=True)
    firstname = models.CharField(max_length=20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

