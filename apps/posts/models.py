from django.db import models

from apps.users.models import User


class Post(models.Model):
    title = models.CharField(
        max_length=255,
        null=True, blank=True,
        verbose_name='Название'
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name='Описание'
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    image = models.ImageField(
        null=True, blank=True,
        upload_to='post_image/',
        verbose_name='Картинка')

    likes = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Лайки'
    )
    dislikes = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Дизлайки'
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ("-id",)

    def __str__(self):
        return f'{self.title}'
