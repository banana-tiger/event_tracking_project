# event_tracking_project
----

Для запуска из cmd:
```
set EVENT_TRACKING_SECRET_KEY='lolkek' && set FLASK_APP=src\event_tracking_project && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run 
```

```
export EVENT_TRACKING_SECRET_KEY='lolkek' \
&& export FLASK_APP=src/event_tracking_project \
&& export FLASK_ENV=development && flask run
```

### Миграция
Перед миграцией необходимо импортировать модели в файл migrator.py и создать миграцию командой ниже, заменив #migration message 
```
set EVENT_TRACKING_SECRET_KEY='lolkek' && set FLASK_APP=migrator.py && flask db migrate -m "#migration message"
```

```export EVENT_TRACKING_SECRET_KEY='lolkek' && set FLASK_APP=migrator.py && flask db migrate -m "#migration message"```