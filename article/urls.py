from django.urls import include, path
from rest_framework import routers

from article.views import ArticleViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r"article", ArticleViewSet)
router.register(r"comment", CommentViewSet)

extra_patterns = [
    path("", include(router.urls)),
]

urlpatterns = [
    path("v1/", include(extra_patterns)),
]
