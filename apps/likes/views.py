from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from apps.likes.serializers import LikesSerializer, DisLikesSerializer
from apps.likes.models import Likes, DisLikes
from apps.likes.filters import DateLikesFilter, DateDisLikesFilter


class LikesModelViewSet(ListAPIView):
    queryset = Likes.objects.all()
    serializer_class = LikesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DateLikesFilter


class DisLikesModelViewSet(ListAPIView):
    queryset = DisLikes.objects.all()
    serializer_class = DisLikesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DateDisLikesFilter