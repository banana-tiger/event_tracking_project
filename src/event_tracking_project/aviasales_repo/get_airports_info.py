from src.event_tracking_project import create_app
from src.event_tracking_project.aviasales_repo.aviasales_api_utils import fetch_json
from src.event_tracking_project.aviasales_repo.config import AVIASALES_API_AIRPORTS_URL
from src.event_tracking_project.aviasales_repo.models import Airport
from src.event_tracking_project.db import db


# JSON аэропортов это не только аэропорты но еще и жд вокзалы и прочее, признак flightable = True показывает,
# является ли действующим аэропортом

# @dataclass()
# class Airport:
#     name: str
#     code: str
#     country_code: str
#     codes_combo: str
#     flightable: bool

airport = Airport()


def dump_airport_in_db(airport: Airport=airport):
    new_airport = Airport(
        name=airport.name,
        code=airport.code,
        country_code=airport.country_code,
        codes_combo=airport.codes_combo,
        flightable=airport.flightable
    )
    db.session.add(new_airport)
    db.session.commit()


if __name__ == '__main__':

    app = create_app()

    airports = fetch_json(AVIASALES_API_AIRPORTS_URL)

    with app.app_context():
        for airport in airports:
            airport_codes_combo = airport['code'] + airport['country_code']
            city_for_db = Airport(
                name=airport['name'],
                code=airport['code'],
                country_code=airport['country_code'],
                codes_combo=airport_codes_combo,
                flightable=airport['flightable'])

            dump_airport_in_db(city_for_db)
