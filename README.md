# Flask-приложение
Данное приложение создано в рамках изучения Flask. 

Сайт занимается постоянным сбором новостей (Celery с использованием Redis) с сайта [habr.com](https://habr.com/ru/search/?target_type=posts&q=python&order_by=date), отображает текущую погоду, а также имеет функционал регистрации/авторизации пользователей и возможность комментировать посты.

В качестве базы данных используется SQLite, работающая через ORM SQLAlchemy.
## Установка
Создайте и активируйте виртуальное окружение, установите необходимые библиотеки:
```python
pip install -r requirements.txt
```
## Настройка
Создайте файл config.py на основе config.py.default, добавьте следующие настройки:
```python
from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = '' # Moscow,Russia
WEATHER_API_KEY = '' # from https://www.worldweatheronline.com/developer/api/
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = '' # random string

REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False
```
## Запуск
Запуск приложения будем производить через скрипт.

1. Для Windows:

   В корне проекта создаем файл run.bat. В файл добавляем строку:
   ```python
   set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
   ```
    Теперь для запуска проекта нужно просто в активированном виртуальном окружении написать в консоли run.bat или run.

 2. Для Linux и MacOS:
 
    В корне проекта создадим файл run.sh:
   ```python
   #!/bin/sh
   export FLASK_APP=webapp && export FLASK_ENV=development && flask run
   ```
   Сохраните файл и в корне проекта выполните в консоли команду:
   ```python
   chmod +x run.sh
   ```
   это сделает файл исполняемым.
   
   Теперь для запуска проекта нужно писать:
   ```python
   ./run.sh
   ```