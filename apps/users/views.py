from rest_framework import viewsets

from apps.users import models
from apps.users import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

