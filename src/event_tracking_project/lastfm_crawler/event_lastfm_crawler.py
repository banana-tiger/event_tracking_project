from datetime import datetime
import typing

import requests
from bs4 import BeautifulSoup

from ..db import db
from .model import Event
from ..user.model import Artists


def prepare_artist_name(artist_name: str) -> str:
    artist = '+'.join(artist_name.split())
    return artist


def get_html(url: str) -> str:
    result = requests.get(url)
    result.raise_for_status()
    return result.text


def fetch_events_by_artist(artist: Artists) -> typing.List[Event]:
    artist_name = artist.artist_name
    url = f"https://www.last.fm/ru/music/{prepare_artist_name(artist_name)}/+events"

    try:
        html = get_html(url)

        soup = BeautifulSoup(html, 'html.parser')
        event_list = soup.select('.events-list-item')

        all_events = []
        for event in event_list:
            event_date_element = event.select_one('.events-list-item-date')
            if event_date_element:
                event_date = datetime.fromisoformat(event_date_element['content'])
            else:
                event_date = None

            place = ' '.join(event.select_one('.events-list-item-venue--title').text.split())

            event_city_country_element = event.select_one('.events-list-item-venue--address').text.split(',')
            city = ' '.join(event_city_country_element[0].split())
            country = ' '.join(event_city_country_element[1].split())

            status = getattr(event.select_one('.event-list-item-cancelled'), 'text', 'Актуально')

            new_event = Event(event_date=event_date, city=city, country=country, status=status, place=place,
                              title=artist_name, artist_id=artist.artist_id )
            all_events.append(new_event)

        return all_events
    except(requests.RequestException) as e:
        print(e)


def dump_events(new_events: typing.List[Event]):
    for event in new_events:
        if not event.exists_in_db():
            db.session.add(event)
            db.session.commit()
