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

## Acknowledgements

   This project uses wait-for-it.sh, available under the MIT License.

   The MIT License (MIT)
   
   Copyright (c) 2014 Vincent Driessen
   
   Permission is hereby granted, free of charge, to any person obtaining a copy
   of this software and associated documentation files (the "Software"), to deal
   in the Software without restriction, including without limitation the rights
   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
   copies of the Software, and to permit persons to whom the Software is
   furnished to do so, subject to the following conditions:
   
   The above copyright notice and this permission notice shall be included in
   all copies or substantial portions of the Software.
   
   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
   THE SOFTWARE.

# Используемое ПО 
   
   - [wait-for-it.sh](https://github.com/vishnubob/wait-for-it) - используемое по лицензии MIT.

