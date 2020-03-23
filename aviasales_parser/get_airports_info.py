import requests

# JSON аэропортов это не только аэропорты но еще и жд вокзалы и прочее, признак flightable = True показывает,
# является ли действующим аэропортом


def get_airports_info():
    url = 'http://api.travelpayouts.com/data/ru/airports.json'
    try:
        result = requests.get(url)
        result.raise_for_status()
        airports = result.json()
        for airport in airports:
            code = airport['code']
            country_code = airport['country_code']
            flightable = airport['flightable']
            # Не везде есть русское название аэропорта, если нет - берет английское
            if not airport['name']:
                name = airport['name_translations']['en']
            else:
                name = airport['name']

            print(f'{name} - {code} - {country_code} - Действующий аэропорт = {flightable}')
        return False
    except requests.RequestException:
        print('Ошибка сети')
        return False


def save_city_in_db(city):
    return False


if __name__ == '__main__':
    get_airports_info()