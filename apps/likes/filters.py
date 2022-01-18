from django_filters import rest_framework as filters
from apps.likes.models import Likes, DisLikes


class DateLikesFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="created_at__date", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="created_at__date", lookup_expr="lte")

    class Meta:
        model = Likes
        fields = ['start_date', 'end_date']


class DateDisLikesFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="created_at__date", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="created_at__date", lookup_expr="lte")

    class Meta:
        model = DisLikes
        fields = ['start_date', 'end_date']