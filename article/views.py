from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from article.models import Article, Comment
from article.schema.schema_extension import (POST_ARTICLE_RESPONSE,
                                             POST_COMMENT_RESPONSE)
from article.schema.serializers_for_schema import (ArticleForSchemaSerializer,
                                                   CommentForSchemaSerializer)
from article.serializers import (ArticleCreateSerializer, ArticleSerializer,
                                 CommentCreateSerializer, CommentSerializer)

User = get_user_model()


@extend_schema_view(
    retrieve=extend_schema(responses=ArticleForSchemaSerializer),
    create=extend_schema(responses=POST_ARTICLE_RESPONSE),
)
class ArticleViewSet(
    mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ("create", "update", "partial_update"):
            return ArticleCreateSerializer
        return self.serializer_class


@extend_schema_view(
    retrieve=extend_schema(responses=CommentForSchemaSerializer),
    create=extend_schema(responses=POST_COMMENT_RESPONSE),
)
class CommentViewSet(
    mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ("create", "update", "partial_update"):
            return CommentCreateSerializer
        return self.serializer_class
