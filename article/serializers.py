from django.contrib.auth import get_user_model
from rest_framework import serializers

from article.models import COMMENT_ERROR_TEXT, Article, Comment

User = get_user_model()


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ["author"]


class ArticleSerializer(serializers.ModelSerializer):

    comments = serializers.SerializerMethodField()
    author = serializers.CharField(source="author.username")

    class Meta:
        model = Article
        fields = "__all__"

    def get_comments(self, obj):
        comments = obj.comments.filter(level=1)
        return CommentForArticleSerializer(comments, many=True).data


class CommentBaseSerializer(serializers.ModelSerializer):

    comments = serializers.SerializerMethodField()
    author = serializers.CharField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "author", "article", "level", "text", "comments"]

    def get_comments(self, obj):
        pass


class CommentForArticleSerializer(CommentBaseSerializer):
    def get_comments(self, obj):
        if obj.level == 3:
            return None
        comments = obj.comments.all()
        return CommentForArticleSerializer(comments, many=True).data


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author"]

    def validate(self, data):
        if data["article"] != data["comment"].article:
            raise serializers.ValidationError(COMMENT_ERROR_TEXT)
        return data


class CommentSerializer(CommentBaseSerializer):
    def get_comments(self, obj):
        comments = obj.comments.all()
        return CommentSerializer(comments, many=True).data
