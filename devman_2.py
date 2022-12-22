import requests
from urllib.parse import urlparse, urlunparse


long_url = str(input())


def shorten_url(token):

    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
    }
    data = {
        'long_url': f'{long_url}',
        'domain': 'bit.ly'
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()['link']


try:
    shorten_url('e95f9ad0d5aa637b6180d947839bd17fc8310ee9')
except requests.exceptions.HTTPError as error:
    exit("Can't get data from server:\n{0}".format(error))
print('Битлинк ', shorten_url('e95f9ad0d5aa637b6180d947839bd17fc8310ee9'))


def count_clicks(token, short_url):  #короче в эту функцию мне вроде как надо передавать результат верхней

    url = 'https://api-ssl.bitly.com/v4/bitlinks/bit.ly/3G9xPdl/clicks/summary'
    parsed_url = urlparse(url)
    path = f'/v4/bitlinks/{shorten_url("e95f9ad0d5aa637b6180d947839bd17fc8310ee9")[8:]}/clicks/summary' #вот здесь еще хуйня типа при вызове верхней функции передается ссылка полностью, а мне надо без https://
    new_parsed_url = parsed_url._replace(path=path)
    user_url = urlunparse(new_parsed_url)
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = (
        ('unit', 'day'),
        ('units', '-1')
    )
    response = requests.get(user_url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


try:
    test = count_clicks('e95f9ad0d5aa637b6180d947839bd17fc8310ee9', shorten_url('e95f9ad0d5aa637b6180d947839bd17fc8310ee9'))
except requests.exceptions.HTTPError as error:
    exit("Can't get data from server:\n{0}".format(error))
print('количество кликов ', count_clicks('e95f9ad0d5aa637b6180d947839bd17fc8310ee9', shorten_url('e95f9ad0d5aa637b6180d947839bd17fc8310ee9')))
