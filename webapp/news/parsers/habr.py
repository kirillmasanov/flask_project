from datetime import datetime, timedelta
import locale
import platform

from bs4 import BeautifulSoup

from webapp.db import db
from webapp.news.models import News
from webapp.news.parsers.utils import get_html, save_news

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, 'russian')
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU.utf8')

dict_month = {
    'января': 'Январь',
    'февраля': 'Февраль',
    'марта': 'Март',
    'апреля': 'Апрель',
    'мая': 'Май',
    'июня': 'Июнь',
    'июля': 'Июль',
    'августа': 'Август',
    'сентября': 'Сентябрь',
    'октября': 'Октябрь',
    'ноября': 'Ноябрь',
    'декабря': 'Декабрь'
}


def parse_habr_date(date_str):
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    else:
        date_list = date_str.split()
        month = date_list[1]
        if month in dict_month:
            date_list[1] = dict_month[month]
            date_str = ' '.join(date_list)
    try:
        return datetime.strptime(date_str, '%d %B %Y в %H:%M')
    except ValueError:
        return datetime.now()


def get_news_snippets():
    url = 'https://habr.com/ru/search/?target_type=posts&q=python&order_by=date'
    html = get_html(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='content-list_posts').find_all('li', class_='content-list__item_post')
        result_news = []
        for news in all_news:
            title = news.find('a', class_='post__title_link').text
            url = news.find('a', class_='post__title_link')['href']
            published = news.find('span', class_='post__time').text
            published = parse_habr_date(published)
            save_news(title, url, published)


def get_news_content():
    news_without_text = News.query.filter(News.text.is_(None))
    for news in news_without_text:
        html = get_html(news.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            article = soup.find('div', class_='post__text-html').decode_contents()
            if article:
                news.text = article
                db.session.add(news)
                db.session.commit()
