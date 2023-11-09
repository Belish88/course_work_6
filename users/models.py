from django.contrib.auth.models import AbstractUser
from django.db import models

from users.utils import create_token

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    first_name = models.CharField(max_length=50, **NULLABLE, verbose_name='фамилия')
    last_name = models.CharField(max_length=50, **NULLABLE, verbose_name='имя')
    token = models.CharField(max_length=100, default=create_token(), verbose_name='token')
    email_verify = models.BooleanField(default=False, verbose_name='верификация почты')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

