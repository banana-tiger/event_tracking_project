from .event_lastfm_crawler import fetch_events_by_artist, dump_events


def all_events(artists: list) -> None:
    for artist in artists:
        events = fetch_events_by_artist(artist)
        dump_events(events)


def get_events_by_artist(artist):
    events = fetch_events_by_artist(artist)
    dump_events(events)


if __name__ == '__main__':
    from src.event_tracking_project import create_app
    app = create_app()
    with app.app_context():
        all_events(['Twenty One Pilots'])
