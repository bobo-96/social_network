from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.posts.views import PostView, PostLikeView, PostLikesView, PostDisLikesView, PostDisLikeView, PostLikeViewList

router = DefaultRouter()

router.register('', PostView, basename='post')

urlpatterns = [
    path('<int:pk>/like/', PostLikeView.as_view()),
    path('<int:pk>/likes_list/', PostLikesView.as_view()),
    path('<int:pk>/dislike/', PostDisLikeView.as_view()),
    path('<int:pk>/dislikes_list/', PostDisLikesView.as_view()),
    path('likes_by_day/', PostLikeViewList.as_view({'get': 'list'}))

]

urlpatterns += router.urls
