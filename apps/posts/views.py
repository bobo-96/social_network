from rest_framework import viewsets

from apps.posts.mixins import DisLikeMixins, LikeMixins
from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostView(LikeMixins, DisLikeMixins, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
