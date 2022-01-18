from django.db import models
from apps.posts.models import Post
from apps.users.models import User


class Likes(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Лайки"
        verbose_name_plural = "Лайк"

    def __str__(self):
        return f"{self.author.username} -- {self.post.title} -- {self.created_at}"


class DisLikes(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='dislike')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = "Дизлайки"
        verbose_name_plural = "Дизлайк"

    def __str__(self):
        return f"{self.author.username} -- {self.post.title} -- {self.created_at}"