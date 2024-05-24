import os
from .settings import *  # импортируйте все настройки из основного файла settings.py
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key-for-testing')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',  # используйте in-memory базу данных SQLite для тестов (быстрее!)
    }
}