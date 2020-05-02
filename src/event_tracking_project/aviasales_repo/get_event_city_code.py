from sqlalchemy import or_

from src.event_tracking_project import create_app
from src.event_tracking_project.aviasales_repo.models import Country, City
from src.event_tracking_project.lastfm_crawler.model import Event
from src.event_tracking_project.lastfm_crawler.event_lastfm_crawler import fetch_events_by_artist

app = create_app()

NA_MESSAGE = 'IATA City Code is Not Available'


def get_event_city_code(event: Event):
    event_city = event.city
    city_filter = or_(City.name == event_city,
                      City.de_name == event_city,
                      City.es_name == event_city,
                      City.fr_name == event_city,
                      City.it_name == event_city,
                      City.ru_name == event_city)
    # country_filtered = Country.query.filter(Country.name == event.country)
    event_city = City.query.join(Country).filter(Country.name == event.country).filter(city_filter).first()
    if not event_city:
        return NA_MESSAGE
    else:
        event_city_code = event_city.code
        return event_city_code


if __name__ == '__main__':
    with app.app_context():
        test_events = fetch_events_by_artist("Enter Shikari")
        for event in test_events:
            print(get_event_city_code(event))
