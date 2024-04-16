Sport Health API

Это RESTful API платформы "Спорт и Здоровье", предоставляющее простые и понятные возможности для управления пользователями, их профилями, фитнес-активностями и целями. Вы можете регистрировать новых пользователей, добавлять фитнес-активности, устанавливать цели, получать информацию о профилях и многое другое. Для безопасности доступа к API требуется аутентификация с использованием токенов.


## Используемые технологии

- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) Django: Мощный веб-фреймворк на Python.
- ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) Django REST Framework: Библиотека для создания API на основе Django.
- ![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white) Swagger: Инструмент для создания интерактивной документации API.

## Как начать

1) Склонируйте репозиторий:
 
```
git clone https://github.com/husniddin02/Sport-Health-API.git

```
2) Создайте виртуальное окружение: 
```
python -m venv .venv
```
3) Активируйте виртуальное окружение: 
```
source .venv/bin/activate  # На Windows используйте `.venv\Scripts\activate`

```
4) Установите зависимости:
```
pip install -r requirements.txt
```
5) Примените миграции: 
```
python manage.py makemigrations
python manage.py migrate
```
6) Создайте суперпользователя:
```
python manage.py createsuperuser
```
7) Запустите сервер разработки: 
```
python manage.py runserver
```

Open Swagger API documentation [localhost:8000/swagger/](http://localhost:8000/swagger/)