from src.event_tracking_project.server_event import app


def run_app():
    app.run(debug=True)


if __name__ == '__main__':
    run_app()