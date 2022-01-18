from rest_framework.routers import DefaultRouter

from apps.posts.views import PostView

router = DefaultRouter()

router.register('', PostView, basename='post')

urlpatterns = router.urls
