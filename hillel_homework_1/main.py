# -*- coding: utf-8 -*-
from os import environ
import requests
from requests import JSONDecodeError

DOMAIN = environ.get('DOMAIN', 'http://127.0.0.1:5000')


def parse(query: str) -> dict:
    response = requests.get(query)
    try:
        return response.json()
    except JSONDecodeError:
        return {"status_code": response.status_code}


def parse_cookie(query: str) -> dict:
    response = requests.get(f'{DOMAIN}/?{query}')
    return dict(response.cookies)


if __name__ == '__main__':
    assert parse(f'{DOMAIN}/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse(f'{DOMAIN}/path/to/page?name=zelen&color=purple&') == {'name': 'zelen', 'color': 'purple'}
    assert parse(f'{DOMAIN}/') == {}
    assert parse(f'{DOMAIN}/?') == {}
    assert parse(f'{DOMAIN}/?name=Dima') == {'name': 'Dima'}
    assert parse(f'{DOMAIN}/?name=Dima;') == {'name': 'Dima'}
    assert parse(f'{DOMAIN}/name=Dima;') == {'status_code': 404}
    assert parse(f'{DOMAIN}/?name=Dima;age=30') == {'name': 'Dima', 'age': '30'}
    assert parse(f'{DOMAIN}/?name=Dima;age=30&last_name=Davidov') == {'name': 'Dima', 'age': '30', 'last_name': 'Davidov'}
    assert parse(f'{DOMAIN}/?name=Dima===user&name=Maks') == {'name': 'Dima===user'}

    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('&;') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Python;version=3.4.5;') == {'name': 'Python', 'version': '3.4.5'}
    # will return always " in '
    assert parse_cookie('name=Python;version=3.4.5%20+') == {'name': 'Python', 'version': '"3.4.5  "'}
    assert parse_cookie('name=Python+++;version=3.4.5') == {'name': '"Python   "', 'version': '3.4.5'}
    assert parse_cookie('name=Python+++;;;;;;&&&version=3.4.5') == {'name': '"Python   "', 'version': '3.4.5'}
    assert parse_cookie('name=Python;;;;;;&&&') == {'name': 'Python'}
