import os
import requests

from urllib.parse import urlparse

BITLY_TOKEN = os.environ['BITLY_TOKEN']


def get_url_without_scheme(url):
  url = urlparse(url)
  url = f'{url.netloc}{url.path}'

  return url


def shorten_link(long_url, token):
    url_bitly = 'https://api-ssl.bitly.com/v4/bitlinks'

    headers = {
        'Authorization': token,
    }

    payload = {
        'long_url': long_url
    }
    
    response = requests.post(url_bitly, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()['link']


def count_clicks(url, token):
    url = get_url_without_scheme(url)

    url_bitly = \
        f'https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary'

    headers = {
        'Authorization': token,
    }

    response = requests.get(url_bitly, headers=headers)
    response.raise_for_status()

    return response.json()['total_clicks']


def is_bitlink(url, token):
    url = get_url_without_scheme(url)

    url_bitly = \
        f'https://api-ssl.bitly.com/v4/bitlinks/{url}'

    headers = {
        'Authorization': token,
    }

    response = requests.get(url_bitly, headers=headers)

    return response.ok


if __name__ == '__main__':
  user_link = input('Введите ссылку\n')

  try:
    if is_bitlink(user_link, BITLY_TOKEN):
      print(count_clicks(user_link, BITLY_TOKEN))
    
    else:
      print(shorten_link(user_link, BITLY_TOKEN))
      
  except requests.exceptions.HTTPError:
    print('Ваша ссылка не верна, попробуйте еще раз...')