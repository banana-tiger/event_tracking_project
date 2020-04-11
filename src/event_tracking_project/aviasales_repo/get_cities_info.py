from dataclasses import dataclass

from src.event_tracking_project import create_app
from src.event_tracking_project.aviasales_repo.aviasales_api_utils import fetch_json
from src.event_tracking_project.aviasales_repo.config import AVIASALES_API_CITIES_URL
from src.event_tracking_project.aviasales_repo.models import Cities
from src.event_tracking_project.db import db


@dataclass()
class City:
    name: str
    code: str
    country_code: str
    codes_combo: str


def save_city_in_db(City):
    new_city = Cities(
        name=City.name,
        code=City.code,
        country_code=City.country_code,
        codes_combo=City.codes_combo
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

            save_city_in_db(city_for_db)
