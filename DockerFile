# Используем базовый образ python
FROM python:3.12

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в рабочую директорию
COPY requirements.txt /app/

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в рабочую директорию контейнера
COPY . /app/

# Устанавливаем переменные окружения для Django
ENV PYTHONUNBUFFERED=1

# Создаём директорию для медиа файлов
RUN mkdir -p /app/media

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Команда запускается при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--nothreading", "--noreload"]