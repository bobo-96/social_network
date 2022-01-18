from rest_framework import serializers

from apps.posts.models import Post
from apps.users.serializers import UserDetailSerializer


class PostSerializer(serializers.ModelSerializer):
    owner = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'created_on', 'image', 'owner', 'likes', 'dislikes']

        read_only_fields = ('id','likes', 'dislikes', 'created_on')

    def create(self, validated_data):
        user = self.context.get('request').user
        post = Post.objects.create(owner=user, **validated_data)
        return post


