import random

from dicts.calculate import common_currencies, uncommon_currencies


def random_currency(symbol: str, conversation_pairs_len: int):
    """
    This algorithm was based on current method realisation, it could be wrong

    :param symbol: two currencies conversion string
    :param conversation_pairs_len: how many conversions we'd like to make [1,3]
    :return: random currency with selected conversation pair
    """
    selected_currencies = {symbol[0:3], symbol[3:6]}

    if 1 == conversation_pairs_len:
        return random.choice(selected_currencies)
    else:
        uncrossed_currencies = common_currencies - selected_currencies
        if 2 == conversation_pairs_len:
            return random.choice(uncrossed_currencies)
        else:
            return random.choice(uncommon_currencies - selected_currencies)
