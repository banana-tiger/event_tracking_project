from sqlalchemy import or_

from src.event_tracking_project import create_app
from src.event_tracking_project.lastfm_crawler.event_lastfm_crawler import fetch_events_by_artist
from src.event_tracking_project.aviasales_repo.models import Country, City

app = create_app()


def get_event_city_code(artist):
    events_list = fetch_events_by_artist(artist)
    for number, event in enumerate(events_list):
        city_filter = or_(City.name == event.city,
                          City.de_name == event.city,
                          City.es_name == event.city,
                          City.fr_name == event.city,
                          City.it_name == event.city,
                          City.ru_name == event.city)
        # country_filtered = Country.query.filter(Country.name == event.country)
        event_city = City.query.join(Country).filter(Country.name == event.country).filter(city_filter).first()
        if not event_city:
            print("{}. {} in {}. IATA code - N/A".format(number, event.city, event.country))
        else:
            print("{}. {} in {}. IATA code - {}".format(number, event.city, event.country, event_city.code))


if __name__ == '__main__':
    with app.app_context():
        get_event_city_code("Rammstein")
