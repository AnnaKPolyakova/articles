from rest_framework import serializers
from article.serializers import ArticleSerializer, CommentForArticleSerializer, \
    CommentSerializer


class CommentForArticleForSchemaSerializer(CommentForArticleSerializer):
    comments = serializers.ListField()


class ArticleForSchemaSerializer(ArticleSerializer):
    comments = serializers.ListField(child=CommentForArticleForSchemaSerializer())


class CommentForSchemaSerializer(CommentSerializer):
    comments = serializers.ListField(child=CommentForArticleForSchemaSerializer())
