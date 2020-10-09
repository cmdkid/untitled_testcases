import requests
import urllib.parse
from json import JSONDecodeError

from src.antiDdosTimer import timer


def make_request(_type: str, url: str, data: dict, **kwargs):
    headers = None
    if 'headers' in kwargs.items():
        headers = kwargs['headers']

    timeout_time = 30
    if 'timeout' in kwargs.items() and type(kwargs['timeout']) == type(int):
        timeout_time = kwargs.get('timeout')

    timer.background_pause()  # stay 5 sec wait between requests to avoid DDoS protection
    if 'GET' == _type:
        """
        return (200, {'commission': None, 'conversion_pairs': {'AUDUSD': 0s.71628, 'USDCAD': 1.32044}, 'long': '-0.07',
                      'lots_mln_usd': '14.76', 'margin': '358.14',
                      'margin_formula1': 'Lots x Contract size x Required margin',
                      'margin_formula2': '0.10 x 100000.0 x 5.0% = 500.000 AUD', 'no_quotes': False, 'profit': '0.76',
                      'profit_formula1': 'Point size x Contract size x Lots',
                      'profit_formula2': '0.00010 x 100000.0 x 0.10 = 1.00 CAD', 'short': '-0.12', 'swap_char': 'pt.',
                      'swap_enable': True, 'swap_formula1': 'Lots x Contract size x Short_or_Long x Point size',
                      'swap_formula2': '0.10 x 100000.0 x -0.08590 x 0.00010 = -0.09 CAD',
                      'swap_formula3': '0.10 x 100000.0 x -0.15690 x 0.00010 = -0.16 CAD', 'swap_long': '-0.09',
                      'swap_short': '-0.16', 'tick_size': 0, 'user_currency': 'USD',
                      'volume_formula1': 'Lots x Contract size', 'volume_formula2': '0.10 x 100000 = 10000.00 AUD',
                      'volume_mln_usd': '0.0072', 'form_type': 'classic'})
        """
        if 0 == len(data):
            request_link = url
        else:
            request_link = f'{url}?{urllib.parse.urlencode(data)}'

        response = requests.get(request_link, headers=headers, timeout=timeout_time)
    else:
        err_msg = f'Wrong request type {type}'
        raise ValueError(err_msg)

    if 200 <= response.status_code < 300:
        try:
            return response.status_code, response.json()
        except JSONDecodeError:
            return response.status_code, response
    else:
        return response.status_code, response


def http_get(url: str, data: dict, **kwargs):
    return make_request('GET', url, data)
