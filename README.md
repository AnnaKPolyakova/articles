# articles

API для создания/получения статей и комментариев к ним

Технологии и требования:
```
Python 3.9+
Django
Django REST Framework
Poetry
```

Запуск проекта
```
1) Скачать проект с гитхаб
2) Создаем в корне .env и добавляем в него следующие данные:

DB_NAME=     
POSTGRES_USER=      
POSTGRES_PASSWORD=      
DB_HOST=db
DB_PORT=5432
DJANGO_SECRET_KEY=


3) Разворачиваем и запускаем проект:
- docker compose up
- docker-compose exec web python manage.py migrate --noinput   # применяем миграции
- docker-compose exec web python manage.py createsuperuser     # создаем суперпользователя
- docker-compose exec web python manage.py collectstatic --no-input     # собираем статику
```

Автодокументация
```
http://127.0.0.1/api/schema/swagger-ui/
```
