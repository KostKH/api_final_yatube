# api_final_yatube

API для учебного проекта Yatube - социальной сети для публикации и чтения постов, а также комментариев к ним.

Реализован REST API CRUD для основных моделей проекта, для аутентификации примненяется JWT-токен. В проекте реализованы пермишены, фильтрации, сортировки и поиск по запросам клиентов, реализована пагинация ответов от API, установлено ограничение количества запросов к API.

## Системные требования
- Python 3.7+
- Works on Linux, Windows, macOS

## Технологии:
- Python 3.7
- Django 2.2.6
- Django REST Framework
- Simple-JWT

## Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/KostKH/api_final_yatube.git
cd api_final_yatube
```

- Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/scripts/activate
python -m pip install --upgrade pip
```

- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
cd yatube_api
```
- Выполнить миграции и запустить проект:
```
python manage.py migrate
python manage.py runserver
```

## Документация по API
Документаци доступна по эндпойнту /redoc/

## Примеры

Список доступных эндпоинтов:

```
api/v1/posts/ - получение списка постов (GET), публикация поста (POST)
api/v1/posts/{id}/ - управление постом (GET, PUT, PATCH, DELETE)
api/v1/posts/{post_id}/comments/ - получение списка комментариев (GET), публикация комментария (POST)
api/v1/posts/{post_id}/comments/{id}/  - управление комментарием (GET, PUT, PATCH, DELETE)
api/v1/follow/ - Подписки пользователя (GET, POST)
api/v1/jwt/create/ - Получение JWT-токена
api/v1/jwt/refresh/ - Обновление JWT-токена
api/v1/jwt/verify/ - Проверка JWT-токена
```