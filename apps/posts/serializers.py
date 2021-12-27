from rest_framework import serializers

from apps.posts.models import Post, PostLike
from apps.users.serializers import UserDetailSerializer


class PostSerializer(serializers.ModelSerializer):
    owner = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'created_on', 'image', 'owner']

    def create(self, validated_data):
        user = self.context.get('request').user
        post = Post.objects.create(owner=user, **validated_data)
        return post


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'post', 'user', 'liked_on']


class LikeByDaySerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField()
    likes = serializers.IntegerField()
    post = PostSerializer(read_only=True)

    class Meta:
        model = PostLike
        fields = ('date', 'likes', 'post')