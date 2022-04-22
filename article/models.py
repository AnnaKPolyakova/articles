from django.contrib.auth import get_user_model
from django.db import models
from django.core.exceptions import ValidationError

User = get_user_model()

COMMENT_ERROR_TEXT = (
    "Указанная статья и статья у головного комментария должны быть одинаковые"
)


class Article(models.Model):

    title = models.CharField(
        max_length=40,
        verbose_name="Название",
        help_text="Не более 40 символов",
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="article",
        verbose_name="Автор",
    )

    text = models.TextField(
        verbose_name="Текст"
    )

    pub_date = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ("pub_date",)
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Статья"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор"
    )
    comment = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="комментарий"
    )
    level = models.PositiveIntegerField(
        default=1
    )
    pub_date = models.DateTimeField(
        auto_now=True,
        verbose_name="Дату публикации комментария"
    )
    text = models.TextField(
        verbose_name="Текст отзыва",
    )

    def clean(self):
        if self.comment is not None:
            if self.comment.article != self.article:
                raise ValidationError(COMMENT_ERROR_TEXT)
            self.level = self.comment.level + 1

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
