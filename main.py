import argparse
import requests

from urllib.parse import urlparse

from environs import Env


def createParser ():
    parser = argparse.ArgumentParser (
        description='Сократим ссылку либо вернем клики по ней'
    )
    parser.add_argument ('link', help='Ваша ссылка')
 
    return parser


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
  env = Env()
  env.read_env()

  bitly_token = env('BITLY_TOKEN')

  parser = createParser()
  namespace = parser.parse_args()
  user_link = namespace.link

  try:
    if is_bitlink(user_link, bitly_token):
      print(count_clicks(user_link, bitly_token))
    
    else:
      print(shorten_link(user_link, bitly_token))
    
  except requests.exceptions.HTTPError:
    print('Ваша ссылка не верна, попробуйте еще раз...')
