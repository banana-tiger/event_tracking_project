from dataclasses import dataclass

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


def dump_city_in_db(city: City=city):
    new_city = City(
        name=city.name,
        code=city.code,
        country_code=city.country_code,
        codes_combo=city.codes_combo
    )
    db.session.add(new_city)
    db.session.commit()


if __name__ == '__main__':

    app = create_app()

    cities = fetch_json(AVIASALES_API_CITIES_URL)

    with app.app_context():
        for city in cities:
            city_codes_combo = city['code'] + city['country_code']
            city_for_db = City(name=city['name'],
                               code=city['code'],
                               country_code=city['country_code'],
                               codes_combo=city_codes_combo)

            dump_city_in_db(city_for_db)
