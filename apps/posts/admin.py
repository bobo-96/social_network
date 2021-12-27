from django.contrib import admin

from apps.posts.models import Post, PostLike

admin.site.register(Post)
admin.site.register(PostLike)