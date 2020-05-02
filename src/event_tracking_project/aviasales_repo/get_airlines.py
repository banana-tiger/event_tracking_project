from src.event_tracking_project import create_app
from src.event_tracking_project.aviasales_repo.aviasales_api_utils import fetch_json
from src.event_tracking_project.aviasales_repo.config import AVIASALES_API_AIRLINES_URL
from src.event_tracking_project.aviasales_repo.models import Airline
from src.event_tracking_project.db import db


def dump_airline_in_db(airline: Airline):
    new_airline = Airline(
        name=airline.name,
        airline_code=airline.airline_code,
        country=airline.country
    )
    db.session.add(new_airline)
    db.session.commit()


if __name__ == '__main__':

    app = create_app()

    airlines = fetch_json(AVIASALES_API_AIRLINES_URL)

    with app.app_context():
        for al in airlines:
            if not al['country']:
                al_country = "N/A"
            else:
                al_country = al['country']
            airline_for_db = Airline(name=al['name'],
                                     airline_code=al['iata'],
                                     country=al_country)

            dump_airline_in_db(airline_for_db)
