from django.db.models import Count
from django_filters import rest_framework as filters
from rest_framework import viewsets, status, views
from rest_framework.response import Response

from apps.posts.models import Post, PostLike, PostDisLike
from apps.posts.permissions import IsPostOwnerOrReadOnly
from apps.posts.serializers import PostSerializer, PostLikeSerializer, LikeByDaySerializer


class LikeFilter(filters.FilterSet):
    date_from = filters.DateTimeFilter(field_name='liked_on', lookup_expr='gte')
    date_to = filters.DateTimeFilter(field_name='liked_on', lookup_expr='lte')

    class Meta:
        model = PostLike
        fields = ['date_from', 'date_to']


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsPostOwnerOrReadOnly,)


class PostLikesView(views.APIView):

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        likes = PostLike.objects.values_list('user__email', 'liked_on').filter(post=post)
        return Response(likes)


class PostLikeView(views.APIView):

    def get(self, request, pk):
        user = request.user
        post = Post.objects.get(id=pk)
        if PostLike.objects.filter(user=user, post=post).exists():
            PostLike.objects.filter(user=user, post=post).delete()
            return Response('Like Deleted', status=status.HTTP_201_CREATED)
        else:
            PostLike.objects.create(user=user, post=post)
            return Response('Like Created', status=status.HTTP_200_OK)


class PostDisLikesView(views.APIView):

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        dislikes = PostDisLike.objects.values_list('user__email', 'liked_on').filter(post=post)
        return Response(dislikes)


class PostDisLikeView(views.APIView):

    def get(self, request, pk):
        user = request.user
        post = Post.objects.get(id=pk)
        if PostDisLike.objects.filter(user=user, post=post).exists():
            PostDisLike.objects.filter(user=user, post=post).delete()
            return Response('DisLike Deleted', status=status.HTTP_201_CREATED)
        else:
            PostDisLike.objects.create(user=user, post=post)
            return Response('DisLike Created', status=status.HTTP_200_OK)


class PostLikeViewList(viewsets.ModelViewSet):
    queryset = PostLike.objects.extra(
        select={'date': "date(liked_on)"}).annotate(likes=Count('pk'))
    serializer_class = LikeByDaySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LikeFilter
