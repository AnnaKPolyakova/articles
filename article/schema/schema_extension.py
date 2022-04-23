from article.models import COMMENT_ERROR_TEXT
from article.serializers import ArticleCreateSerializer

ERROR_MESSAGES_FOR_POST_ARTICLES = {
    "example": {
        "title": ["Обязательное поле."],
        "text": ["Обязательное поле."],
        "detail": ["Учетные данные не были предоставлены."],
    }
}


ERROR_MESSAGES_FOR_POST_COMMENT = {
    "example": {
        "article": [
            "Обязательное поле.",
            'Недопустимый первичный ключ "{}" - объект не существует.',
            "Некорректный тип. "
            "Ожидалось значение первичного ключа, получен {}",
        ],
        "comment": [
            'Недопустимый первичный ключ "{}" - объект не существует.',
            "Некорректный тип. Ожидалось значение первичного ключа, "
            "получен {}",
        ],
        "text": ["Обязательное поле."],
        "non_field_errors": [COMMENT_ERROR_TEXT],
        "detail": ["Учетные данные не были предоставлены."],
    }
}


POST_ARTICLE_RESPONSE = {
    201: ArticleCreateSerializer,
    400: ERROR_MESSAGES_FOR_POST_ARTICLES,
}


POST_COMMENT_RESPONSE = {
    201: ArticleCreateSerializer,
    400: ERROR_MESSAGES_FOR_POST_COMMENT,
}
