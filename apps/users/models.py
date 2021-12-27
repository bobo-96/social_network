from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.users.manager import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email"
    )
    password_repeat = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    last_activity = models.DateTimeField(
        null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ("-id",)

    def __str__(self):
        return self.email