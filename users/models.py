from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': 'True', 'null': 'True'}


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='email', unique=True)
    country = models.CharField(verbose_name='country', max_length=40, **NULLABLE)
    is_active = models.BooleanField(verbose_name='is_active', default=True)
    is_employee = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
