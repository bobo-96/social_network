from django.core.cache import cache
from django.utils import timezone

from apps.users.models import User


def last_visit_middleware(get_response):
    def middleware(request):

        response = get_response(request)

        if request.session.session_key:
            key = "recently-seen-{}".format(request.session.session_key)
            recently_seen = cache.get(key)

            if not recently_seen and request.user.is_authenticated:
                User.objects.filter(id=request.user.id) \
                    .update(last_activity=timezone.now())

                visit_time = 60 * 30  # 30 minutes
                cache.set(key, 1, visit_time)

        return response

    return middleware
