import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка!')
        return False


def get_python_news():
    url = 'https://www.python.org/blogs/'
    html = get_html(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').find_all('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').get('datetime')
            result_news.append({
                'title': title,
                'url': url,
                'published': published
            })
        return result_news
    return False
