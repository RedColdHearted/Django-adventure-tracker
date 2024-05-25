# Adventure Tracker

*Создание и редактирование меток на карте с функцией авторизации и запуска тестов.*

## Особенности

- ✔️ Реализовано создание и редактирование меток на карте
- ✔️ Настроен запуск тестов при новых коммитах с использованием GitHub Actions
- ✔️ Запуск линтеров при коммите/пуше в GitHub Actions
- ✔️ Сконфигурированы правила для линтеров
- ✔️ Настроен Dockerfile
- ✔️ Настроен docker-compose вместе с PostgreSQL
- ✔️ Приложение запущено на [https://k3ntik.pythonanywhere.com/](https://k3ntik.pythonanywhere.com/) (могут не работать изображения из-за возможной перегрузки сервера)

*Важно:* Авторизация через ВКонтакте не настроена из-за изменений в сервисе авторизации. Вместо этого используется стандартная авторизация Django.

## Установка и запуск

### Локальный запуск

1. Клонируйте репозиторий:
    sh
    git clone https://github.com/RedColdHearted/Django-adventure-tracker
    cd yourrepository
    

2. Создайте и активируйте виртуальное окружение:
    
##sh
    python3 -m venv venv
    source venv/bin/activate  # Для Windows используйте venvScriptsactivate
    

3. Установите зависимости:
    
sh
    pip install -r requirements.txt
    

4. Примените миграции и запустите сервер:
    
sh
    python manage.py migrate
    python manage.py runserver
