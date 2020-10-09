import pytest
from pytest_allure_dsl import allure
from hamcrest import assert_that, is_, equal_to, not_, has_string

from src.requestsHelper import http_get
from dicts.calculate import default_req_data


@pytest.mark.parametrize(
    'header', [
        {'Accept': 'text/html'}
    ]
)
def test_bad_header(allure_dsl, calculate_url, header):
    """
        story: 'Bad header Accept: text/html'
        steps:
            1: 'Send request with bad header {header}'
    """
    with allure_dsl.step(1, header=header):
        status_code, resp_data = http_get(calculate_url, default_req_data, header=header)
        assert_that(status_code, is_(not_(equal_to(200))))

"""
def test_empty_request(allure_dsl, calculate_url):
"""
"""
    story: 'Empty request'
    steps:
        1: 'Send request no data'
"""
"""
    with allure_dsl.step(1):
        status_code, resp_data = http_get(calculate_url, list())
        assert_that(status_code, is_(not_(equal_to(200))))
"""

@pytest.mark.parametrize(
    'field', [
        'form_type',
        'instrument',
        'symbol',
        'lot',
        'leverage',
        'user_currency'
    ]
)
def test_uncompleted_data(allure_dsl, calculate_url, field):
    """
        story: 'Uncompleted data: request without mandatory value'
        steps:
            1: 'Send request without value {field}'
    """
    with allure_dsl.step(1, field=field):
        data = default_req_data.copy()
        data.pop(field, None)
        status_code, resp_data = http_get(calculate_url, data)
        assert_that(status_code, is_(not_(equal_to(200))))
        assert_that(resp_data.text, has_string(f"'{field}': ['This field is required.']"))

@pytest.mark.parametrize(
    'field, values', [
        ('form_type', ["ClassiC", "A", ""]),
        ('instrument', ["foREX", "A", ""]),
        ('symbol', ["AudcaD", "RURRUR", ""]),
        ('lot', [0, -1, 100001, 99999.9999999]),
        ('leverage', [0, -1, 300, 200.0]),
        ('user_currency', ["UsD", "ZZZ", "A", ""])
    ]
)
def test_wrong_valid_type_data(allure_dsl, calculate_url, field, values):
    """
        story: 'Use wrong but valid type data'
        steps:
            1: 'Run request for every value in {values}, while other values stay valid.'
    """
    with allure_dsl.step(1, values=str(values), field=field):
        data = default_req_data.copy()
        for value in values:
            data[field] = value
            status_code, resp_data = http_get(calculate_url, data)
            assert_that(status_code, is_(not_(equal_to(200))))
            assert_that(resp_data.text, has_string(f"'{field}': ['\"{value}\" is not a valid choice.']"))


@pytest.mark.parametrize(
    'value', [
        -1,
        0.0,
        None,
        'Я',
        '.',
        '"',
        '#',
        '\' OR 1=1 -- ',
        'ABCDEFGHIJKLMNOPQSTUVWXYZABCDEFGHIJKLMNOPQSTUVWXYZABCDEFGHIJKLMNOPQSTUVWXYZABCDEFGHIJKLMNOPQSTUVWXYZABCDEFGHIJKLMNOPQSTUVWXYZABCD'
    ]
)
def test_unsupported_data(allure_dsl, calculate_url, value):
    """
        story: 'Use boundary values, but out of order, unsupported values'
        steps:
            1: 'Run request for every filed with value {value}, while other values stay valid.'
    """
    with allure_dsl.step(1, value=str(value)):

        for field in default_req_data.keys():
            data = default_req_data.copy()
            data[field] = value
            status_code, resp_data = http_get(calculate_url, data)
            assert_that(status_code, is_(not_(equal_to(200))))
            # assert_that(resp_data.text, has_string(f"'{field}': ['\"{value}\" is not a valid choice.']"))
