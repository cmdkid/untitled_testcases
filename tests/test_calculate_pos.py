import re
import json
import random
import pytest
from pytest_allure_dsl import allure
from hamcrest import assert_that, is_, equal_to

from schemas.calculate_resp import scheme as calculate_resp_json_schema
from src.requestsHelper import http_get
from src.jsonSchemaHelper import validate_json
from src.datatypesHelper import str_to_float, float_zfill_tail
from src.currencyHelper import random_currency
from dicts.calculate import currencies, symbols, leverages, lot_val_max, lot_val_min, default_req_data


def validate_resp_schema(data):
    return validate_json(calculate_resp_json_schema, data)


def errors_in_formulas(request: dict, response: dict):
    """
    Validate response data in formulas
    :param request: dict with request data
    :param response: dict with response data
    :return: list of validating errors strings, empty list means no errors
    """
    contract_size = 100000.0
    required_margin = 0.05
    point_size = 0.00010
    req_lot = str_to_float(request.get('lot'))

    errors = list()

    margin_formula2 = f"{float_zfill_tail(req_lot, 2)} x {contract_size} x {required_margin * 100}% = {float_zfill_tail(req_lot * contract_size * required_margin, 3)} {request['symbol'][0:3]}"
    if response.get('margin_formula2') != margin_formula2:
        errors.append(f'Expected margin_formula2={margin_formula2}, got={response.get("margin_formula2")}')

    profit_formula2 = f"{float_zfill_tail(point_size, 5)} x {contract_size} x {float_zfill_tail(req_lot, 2)} = {float_zfill_tail(point_size * contract_size * req_lot, 2)} {request['symbol'][3:6]}"
    if response.get('profit_formula2') != profit_formula2:
        errors.append(f'Expected profit_formula2={profit_formula2}, got={response.get("profit_formula2")}')

    pattern = f"{float_zfill_tail(req_lot, 2)} x {contract_size} x -(\\d{{0,10}}\\.{{0,1}}\\d{{0,10}}) x {float_zfill_tail(point_size, 5)} = {response['swap_long']} {request['symbol'][3:6]}"  # is minus default sign it formula?
    regex_result = re.findall(pattern, response['swap_formula2'])
    try:
        swap_long_detailed = regex_result[0]
        swap_formula2 = f"{float_zfill_tail(req_lot, 2)} x {contract_size} x -{float_zfill_tail(swap_long_detailed, 5)} x {float_zfill_tail(point_size, 5)} = {response['swap_long']} {request['symbol'][3:6]}"  # ask business what kind of round algorythm must be used
        if response.get('swap_formula2') != swap_formula2:
            errors.append(f'Expected swap_formula2={swap_formula2}, got={response.get("swap_formula2")}')
    except IndexError:
        errors.append(f'Expected swap_formula2 pattern={pattern}, got={response.get("swap_formula2")}')

    pattern = f"{float_zfill_tail(req_lot, 2)} x {contract_size} x -(\\d{{0,10}}\\.{{0,1}}\\d{{0,10}}) x {float_zfill_tail(point_size, 5)} = {response['swap_short']} {request['symbol'][3:6]}"  # is minus default sign it formula?
    regex_result = re.findall(pattern, response['swap_formula3'])  # must fail, if no regex found
    try:
        swap_long_detailed = regex_result[0]
        swap_formula3 = f"{float_zfill_tail(req_lot, 2)} x {contract_size} x -{float_zfill_tail(swap_long_detailed, 5)} x {float_zfill_tail(point_size, 5)} = {response['swap_short']} {request['symbol'][3:6]}"  # ask business what kind of round algorythm must be used
        if response.get('swap_formula3') != swap_formula3:
            errors.append(f'Expected swap_formula3={swap_formula3}, got={response.get("swap_formula3")}')
    except IndexError:
        errors.append(f'Expected swap_formula3 pattern={pattern}, got={response.get("swap_formula3")}')

    # @review Why contract_size in this formula is rounded, but in others - don't. Is this fail or not?
    volume_formula2 = f"{float_zfill_tail(req_lot, 2)} x {round(contract_size)} = {float_zfill_tail(req_lot * contract_size, 2)} {request['symbol'][0:3]}"
    if response.get('volume_formula2') != volume_formula2:
        errors.append(f'Expected volume_formula2={volume_formula2}, got={response.get("volume_formula2")}')

    return errors


def random_lot():
    lot = random.randint(lot_val_min * 100, lot_val_max * 100) / 100
    if 0 == random.randint(0, 9) % 2:  # make number int for half of requests
        lot = round(lot)
    return lot


def test_default(allure_dsl, calculate_url):
    """
        story: 'Default web request'
        steps:
            1: 'Send request with default web data to {calculate_url}'
            2: 'Send request again to test periodicity of data'
    """
    with allure_dsl.step(1, calculate_url=calculate_url):
        status_code, resp_data = http_get(calculate_url, default_req_data)
        assert_that(status_code, is_(equal_to(200)))
        assert_that(type(resp_data), is_(equal_to(type(dict()))), resp_data.text)
        assert_that(validate_resp_schema(resp_data), is_(equal_to((True, None))))
        assert_that(errors_in_formulas(default_req_data, resp_data), is_(equal_to(list())))

    with allure_dsl.step(2):
        status_code2, resp_data2 = http_get(calculate_url, default_req_data)
        assert_that(status_code2, is_(equal_to(status_code)))
        assert_that(resp_data2, is_(equal_to(resp_data)))


@pytest.mark.parametrize(
    'request_data', [
        {
            'form_type': 'classic',
            'instrument': 'Forex',
            'symbol': random.choice(symbols),
            'lot': lot_val_max,
            'leverage': min(leverages),
            'user_currency': random.choice(currencies),
        },
        {
            'form_type': 'classic',
            'instrument': 'Forex',
            'symbol': random.choice(symbols),
            'lot': lot_val_min,
            'leverage': min(leverages),
            'user_currency': random.choice(currencies),
        },
        {
            'form_type': 'classic',
            'instrument': 'Forex',
            'symbol': random.choice(symbols),
            'lot': lot_val_max,
            'leverage': min(leverages),
            'user_currency': random.choice(currencies),
        },
        {
            'form_type': 'classic',
            'instrument': 'Forex',
            'symbol': random.choice(symbols),
            'lot': lot_val_min,
            'leverage': max(leverages),
            'user_currency': random.choice(currencies),
        },
    ]
)
def test_boundary_values(allure_dsl, request_data, calculate_url):
    """
        story: 'Max and min values of lot and leverage'
        steps:
            1: 'Send request with data {request_data}'
    """
    with allure_dsl.step(1, calculate_url=json.dumps(request_data)):
        status_code, resp_data = http_get(calculate_url, request_data)
        assert_that(status_code, is_(equal_to(200)))
        assert_that(type(resp_data), is_(equal_to(type(dict()))), resp_data.text)
        assert_that(validate_resp_schema(resp_data), is_(equal_to((True, None))))
        assert_that(errors_in_formulas(default_req_data, resp_data), is_(equal_to(list())))


@pytest.mark.parametrize(
    'conversation_pairs_len', [
        1,
        2,
        3
    ]
)
def test_combinations(allure_dsl, calculate_url, conversation_pairs_len):
    """
        story: 'Three combinations of response: user_currency in symbol, user_currency not in symbol, but it's common currency and could be not converted twice, user_currency not in symbol and not common currency (if symbol got "USD" in it,
we got **two** items instead)'
        steps:
            1: 'Send request conversation pairs len {conversation_pairs_len} and data {request_data}'
    """
    symbol = random.choice(symbols)
    request_data = {
        'form_type': 'classic',
        'instrument': 'Forex',
        'symbol': symbol,
        'lot': random_lot(),
        'leverage': random.choice(leverages),
        'user_currency': random_currency(symbol, conversation_pairs_len),
    }
    with allure_dsl.step(1, conversation_pairs_len=conversation_pairs_len, request_data=json.dumps(request_data)):
        status_code, resp_data = http_get(calculate_url, request_data)
        assert_that(status_code, is_(equal_to(200)))
        assert_that(type(resp_data), is_(equal_to(type(dict()))), resp_data.text)
        assert_that(validate_resp_schema(resp_data), is_(equal_to((True, None))))
        assert_that(errors_in_formulas(default_req_data, resp_data), is_(equal_to(list())))
        assert_that(len(resp_data.get('conversion_pairs')), is_(equal_to(conversation_pairs_len)))
