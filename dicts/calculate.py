currencies = ["AED", "AUD", "ARS", "AZN", "BDT", "BHD", "BND", "BRL", "CAD", "CHF", "CLP", "CNY", "COP", "CZK", "DKK",
              "DZD", "EUR", "GEL", "GBP", "GHS", "HKD", "HUF", "IDR", "ILS", "INR", "JOD", "JPY", "KES", "KRW", "KWD",
              "KZT", "LBP", "LKR", "MAD", "MXN", "MYR", "NGN", "NOK", "NZD", "OMR", "PHP", "PKR", "PLN", "QAR", "RON",
              "RUR", "SAR", "SEK", "SGD", "SYP", "THB", "TND", "TRY", "TWD", "UGX", "USD", "UAH", "UZS", "VND", "ZAR",
              "MAU", "MAG", "MPT", "MPD", "MBA", "MBB", "MBC", "MBD"]

symbols = ["AUDCAD", "AUDCHF", "AUDGBP", "AUDJPY", "AUDNZD", "AUDUSD", "CADCHF", "CADJPY", "CHFJPY", "EURAUD", "EURCAD",
           "EURCHF", "EURGBP", "EURJPY", "EURNZD", "EURUSD", "GBPAUD", "GBPCAD", "GBPCHF", "GBPJPY", "GBPNZD", "GBPTRY",
           "GBPUSD", "NZDJPY", "NZDUSD", "USDCAD", "USDCHF", "USDHKD", "USDJPY", "USDMXN", "USDNOK", "USDRUB", "USDSEK",
           "USDTRY", "USDZAR", "XAGUSD", "XAUUSD", "ZARJPY"]

leverages = {200, 100, 88, 50, 20, 10, 2}

# got this limits from web filters, must be reviewed with business
lot_val_max = 100000
lot_val_min = 0.01

default_req_data = {
    'form_type': 'classic',
    'instrument': 'Forex',
    'symbol': 'AUDCAD',
    'lot': '0.1',
    'leverage': '200',
    'user_currency': 'USD',
}

common_currencies = {'CHF', 'EUR', 'AUD', 'CAD', 'DKK', 'GBP', 'HUF', 'JPY', 'MXN', 'NOK', 'NZD', 'PLN', 'SEK', 'SGD', 'TRY', 'USD', 'ZAR'}
uncommon_currencies = set(currencies) - common_currencies
