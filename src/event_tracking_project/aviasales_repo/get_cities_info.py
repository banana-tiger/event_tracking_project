from src.event_tracking_project import create_app
from src.event_tracking_project.aviasales_repo.aviasales_api_utils import fetch_json
from src.event_tracking_project.aviasales_repo.config import AVIASALES_API_CITIES_URL
from src.event_tracking_project.aviasales_repo.models import City
from src.event_tracking_project.db import db

# @dataclass()
# class City:
#     name: str
#     code: str
#     country_code: str
#     codes_combo: str

city = City()


def dump_city_in_db(city: City = city):
    new_city = City(
        name=city.name,
        code=city.code,
        country_code=city.country_code,
        codes_combo=city.codes_combo,
        de_name=city.de_name,
        ru_name=city.ru_name,
        it_name=city.it_name,
        es_name=city.es_name,
        fr_name=city.fr_name,
    )
    db.session.add(new_city)
    db.session.commit()


if __name__ == '__main__':

    app = create_app()

    en_cities = fetch_json(AVIASALES_API_CITIES_URL)
    de_cities = fetch_json(AVIASALES_API_CITIES_URL.replace('en', 'de'))
    ru_cities = fetch_json(AVIASALES_API_CITIES_URL.replace('en', 'ru'))
    it_cities = fetch_json(AVIASALES_API_CITIES_URL.replace('en', 'it'))
    es_cities = fetch_json(AVIASALES_API_CITIES_URL.replace('en', 'es'))
    fr_cities = fetch_json(AVIASALES_API_CITIES_URL.replace('en', 'fr'))
    multy_lang_cities = list(zip(en_cities, de_cities, ru_cities, it_cities, es_cities, fr_cities))

    with app.app_context():
        for city in multy_lang_cities:
            codes_combo = city[0]['code'] + city[0]['country_code']
            complete_city = City(name=city[0]['name'],
                                 code=city[0]['code'],
                                 country_code=city[0]['country_code'],
                                 codes_combo=codes_combo,
                                 de_name=city[1]['name'],
                                 ru_name=city[2]['name'],
                                 it_name=city[3]['name'],
                                 es_name=city[4]['name'],
                                 fr_name=city[5]['name'])
            dump_city_in_db(complete_city)
