from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = 'Moscow,Russia'
WEATHER_API_KEY = '9c1d10e844d04c78831174833201204'
WEATHER_URL = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

SECRET_KEY = 'wdqdwd2e@e2jeiji8904tl@!kdkkbn8@&$^09k'

REMEMBER_COOKIE_DURATION = timedelta(days=5)
