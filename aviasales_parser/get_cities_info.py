import requests


def get_cities_info():
    url = 'http://api.travelpayouts.com/data/en/cities.json'
    try:
        result = requests.get(url)
        result.raise_for_status()
        cities = result.json()
        for city in cities:
            name = city['name']
            code = city['code']
            country_code = city['country_code']
            print(f'{name} - {code} - {country_code}')
        return False
    except requests.RequestException:
        print('Сетевая ошибка')
    return False

def save_city_in_db(city):
    return False

if __name__ == '__main__':
    get_cities_info()
