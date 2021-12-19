from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    birthday = models.DateField(verbose_name='Дата рождения', null=True, blank=True, default=timezone.now)
    address = models.TextField(verbose_name='Адрес проживания', default=None, blank=True, null=True,)

    def __str__(self):
        return self.username