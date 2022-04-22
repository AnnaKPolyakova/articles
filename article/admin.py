from django.contrib import admin
from django.contrib.admin import register

from article.models import Article, Comment


@register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "pub_date",
    )
    list_filter = (
        "author",
        "title",
    )
    search_fields = ("pub_date", "author")


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "article",
        "comment",
        "level",
        "text",
    )
    list_filter = (
        "article",
        "author",
        "comment"
    )

