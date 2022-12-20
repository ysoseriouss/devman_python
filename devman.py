import requests

url_template = 'http://wttr.in/{}'
places = ['Череповец', 'Лондон', 'SVO']
payload = {
    'q': '',
    'n': '',
    'm': '',
    'T': '',
    'M': '',
    'lang': 'ru'
}


for place in places:
    url = url_template.format(place)
    responce = requests.get(url, params=payload)
    responce.raise_for_status()
    print(responce.text)
