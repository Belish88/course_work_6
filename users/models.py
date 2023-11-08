from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    surname = models.CharField(max_length=50, **NULLABLE, verbose_name='фамилия')
    name = models.CharField(max_length=50, **NULLABLE, verbose_name='имя')
    patronymic = models.CharField(max_length=50, **NULLABLE, verbose_name='отчество')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

