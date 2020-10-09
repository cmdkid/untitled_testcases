def str_to_float(s: str, no_exception: bool = True):
    try:
        return float(s)
    except ValueError as e:
        if no_exception:
            return 0.0
        raise ValueError(e)


def float_zfill_tail(number: float, digits_after_dot):
    """
    Add zeros at the end of float number
    :param number: float number
    :param digits_after_dot: number of digits after dot
    :return: string value with enough digits after dot
    """
    data = str(number)
    data = data.split('.')
    if len(data) != 2:
        err_msg = f'"data" is not correct float number!'
        raise ValueError(err_msg)

    current_len = len(data[1])
    if current_len < digits_after_dot:
        data += '0'*(digits_after_dot-current_len)
    return data
