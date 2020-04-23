from src.event_tracking_project import create_app
from src.event_tracking_project.lastfm_crawler.event_lastfm_crawler import fetch_events_by_artist, save_event

def name_artist(artists: list) -> None:
    for artist in artists:
        events = fetch_events_by_artist(artist)
        save_event(events)

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        name_artist(['Rammstein'])

