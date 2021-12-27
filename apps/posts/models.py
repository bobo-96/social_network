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

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ("-id",)

    def __str__(self):
        return f'{self.title}'


class PostLike(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='post_like'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_like'
    )
    liked_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.id}'


class PostDisLike(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='post_dislike',
        null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_dislike',
        null=True, blank=True
    )
    liked_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.id}'
