from src.event_tracking_project import create_app
from src.event_tracking_project.aviasales_repo.aviasales_api_utils import fetch_json
from src.event_tracking_project.aviasales_repo.config import AVIASALES_API_COUNTRIES_URL
from src.event_tracking_project.aviasales_repo.models import Country
from src.event_tracking_project.db import db


def dump_country_in_db(country: Country):
    new_country = Country(
        name=country.name,
        country_code=country.country_code,
    )
    db.session.add(new_country)
    db.session.commit()


if __name__ == '__main__':

    app = create_app()

    countries = fetch_json(AVIASALES_API_COUNTRIES_URL)

    with app.app_context():
        for country in countries:
            country_for_db = Country(name=country['name_translations']['en'],
                                     country_code=country['code'])

            dump_country_in_db(country_for_db)
