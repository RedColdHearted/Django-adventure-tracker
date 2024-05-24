from .settings import *  # импортируйте все настройки из основного файла settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # используйте in-memory базу данных SQLite для тестов (быстрее!)
    }
}