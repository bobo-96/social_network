from apps.users.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", UserViewSet, basename="users")
urlpatterns = router.urls