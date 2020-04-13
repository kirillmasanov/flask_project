from flask import Flask, render_template

from python_org_news import get_python_news
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Новости Python'
    weather = weather_by_city('moscow, russia')
    news_list = get_python_news()
    print(news_list)
    return render_template('index.html', page_title=title, weather=weather, news_list=news_list)


if __name__ == '__main__':
    app.run(debug=True)
