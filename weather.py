import requests


def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    payload = {
        'key': '9c1d10e844d04c78831174833201204',
        'q': city_name,
        'format': 'json',
        'num_of_days': '1',
        'lang': 'ru'
    }
    try:
        response = requests.get(weather_url, params=payload)
        response.raise_for_status()
        weather = response.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except (IndexError, TypeError, ValueError):
                    return False
    except requests.RequestException:
        print('Сетевая ошибка!')
        return False
    return False


if __name__ == '__main__':
    w = weather_by_city('moscow, russia')
    print(w)
