# Adventure Tracker

*Создание и редактирование меток на карте с функцией авторизации и запуска тестов.*

## Особенности

- ✔️ Реализовано создание и редактирование меток на карте
- ✔️ Настроен запуск тестов при новых коммитах с использованием GitHub Actions
- ✔️ Запуск линтеров при коммите/пуше в GitHub Actions
- ✔️ Сконфигурированы правила для линтеров
- ✔️ Настроен Dockerfile
- ✔️ Настроен docker-compose вместе с PostgreSQL
- ✔️ Приложение запущено на [https://k3ntik.pythonanywhere.com/](https://k3ntik.pythonanywhere.com/) (БД - MySQL)

*Важно:* Авторизация через ВКонтакте не настроена из-за изменений в сервисе авторизации. Вместо этого используется стандартная авторизация Django.

## Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий:

    git clone https://github.com/RedColdHearted/Django-adventure-tracker
    <br>
    cd Django-adventure-tracker
    

3. Создайте и активируйте виртуальное окружение:

    
    python3 -m venv venv
    venv/Scripts/activate для windows
    или source .venv/bin/activate для linux


4. Установите зависимости:

    
    pip install -r requirements.txt
    

5. Примените миграции и запустите сервер:
    

    python manage.py migrate
    python manage.py runserver

6. Так же добавьте свои переменные окружение в .env

# Используемое ПО 
   
   - [wait-for-it.sh](https://github.com/vishnubob/wait-for-it)

