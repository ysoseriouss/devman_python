import requests

url_template = 'http://wttr.in/{}'
places = ['Череповец', 'Лондон', 'SVO']
payload = {
    'q': '',
    'n': '',
    'T': '',
    'M': '',
    'lang': 'ru'
}


for place in places:
    url = url_template.format(place)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)
