from dataclasses import dataclass


from src.event_tracking_project.aviasales_repo.config import AVIASALES_API_PRICES_URL
from src.event_tracking_project.aviasales_repo.aviasales_api_utils import fetch_json

# временно заданы константы,
# TODO - импорты, пропущенные через API определения кода, либо коды из базы (города и аэропорты уже есть)
iata_from = 'MOW'
iata_to = '-'

# тоже пока фиксированные значения для тестов
# TODO - импорт из модуля ивентов, для подбора билетов нужен только месяц
#  затем нужно мэтчить даты прилета с датой ивента
depart_date = None
return_date = None

# origin — IATA код города вылета. IATA код указывается буквами верхнего регистра, например MOW.

# destination — IATA код города назначения (укажите "-" для любых направлений).
# IATA код указывается буквами верхнего регистра, например MOW.

# depart_date (не обязательно) — месяц вылета (формат YYYY-MM).
# return_date (не обязательно) — месяц возвращения (формат YYYY-MM).

# token — индивидуальный токен доступа.

# page — необязательный параметр, используется для отображения найденных данных
# (по умолчанию на странице отображается 100 найденных вариантов.
# Если не выбран destination, то данных может быть больше.
# В этом случае используйте page, для отображения следующего набора данных, например, page=2).

# currency — Валюта цен на билеты. Значение по умолчанию — rub. Допустимые значения: [«USD», «EUR», «RUB»].
# TODO - token в переменную окружения

params_aviasales_prices = {'token': '0e3ffa862fa3da9c0d94f2e4d0f80751',
                           'origin': iata_from,
                           'destination': iata_to,
                           'depart_date': depart_date,
                           'return_date': return_date}

# СТРУКТУРА ОТВЕТА
# price — Цена билета (в заданной валюте, параметр currency).
# airline — IATA код авиакомпании, выполняющей перелет.
# flight_number — Номер рейса.
# departure_at — Дата вылета.
# return_at — Дата возвращения.
# expires_at — Дата истечения актуальности найденной цены (UTC+0).


@dataclass
class Ticket:
    price: float
    airline: str
    flight_number: str  # Может быть int
    departure_at: str
    return_at: str
    expires_at: str

fetch_json(AVIASALES_API_PRICES_URL, params_aviasales_prices)

if __name__ == '__main__':
    example_tickets = fetch_json(AVIASALES_API_PRICES_URL, params_aviasales_prices)
    None
