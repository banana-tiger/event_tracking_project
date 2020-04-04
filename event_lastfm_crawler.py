import dataclasses
from datetime import datetime

import requests
from bs4 import BeautifulSoup

@dataclasses.dataclass
class Event:
    event_date: datetime
    city: str
    country: str
    place: str
    status: str
    title: str


def get_artist(name):
    artist = '+'.join(name.split())
    return artist

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Ошибка")
        return False

def get_event_last():
    html = get_html("https://www.last.fm/ru/music/"+get_artist(name='Rammstein')+"/+events")

    if html:
        soup = BeautifulSoup(html, 'html.parser')
        event_list = soup.select('.events-list-item')

        for event in event_list:
            event_date_element = event.select_one('.events-list-item-date')
            if event_date_element:
                event_date = datetime.fromisoformat(event_date_element['content']).strftime('%d.%m.%Y')

            place = ' '.join(event.select_one('.events-list-item-venue--title').text.split())

            event_city_country_element = event.select_one('.events-list-item-venue--address').text.split(',')
            city = ' '.join(event_city_country_element[0].split())
            country = ' '.join(event_city_country_element[1].split())

            status_elemnt = event.select_one('.event-list-item-cancelled')
            if status_elemnt:
                status = status_elemnt.text
            else:
                status = 'Актуально'

            title = get_artist(name='Rammstein')
            print(event_date, title, place, city, country, status)          
            e = Event(event_date=event_date, city=city, country=country, status=status, place=place, title=title)

            

if __name__ == '__main__':
    get_event_last()

