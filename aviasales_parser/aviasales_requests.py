import requests


def get_tickets_by_city(city_code_from, city_code_to):
    tickets_url = 'http://api.travelpayouts.com/v2/prices/latest'

    # currency — валюта цен на билеты.Значение по умолчанию — rub.
    # origin — пункт отправления. IATA код города. Длина 3 символов. Значение по умолчанию LED.
    # destination — пункт назначения. IATA код города. Длина 3 символа. Значение по умолчанию HKT.
    # show_to_affiliates — false — все цены, true — только цены, найденные с партнёрским маркером (рекомендовано).
    # month — первый день месяца, в формате «YYYY-MM-DD». По умолчанию используется месяц, следующий за текущим.
    # trip_duration — длительность пребывания в неделях. Если не указано, то в результате будут билеты в одну сторону.

    params = {
        'token': '0e3ffa862fa3da9c0d94f2e4d0f80751',
        'origin': city_code_from,
        'destination': city_code_to,
        'trip_duration': 1
    }
    try:
        result = requests.get(tickets_url, params=params)
        result.raise_for_status()
        tickets = result.json()
        tickets_list = []
        if tickets['success']:
            for element in tickets['data']:
                ticket = {
                    'depart_date': element['depart_date'],
                    'return_date': element['return_date'],
                    'value': element['value'],
                     }
                tickets_list.append(ticket)
    except requests.RequestException:
        print('Сетевая ошибка')
        return False
    return tickets_list


if __name__ == '__main__':
    print(get_tickets_by_city('MOW', 'LON'))
