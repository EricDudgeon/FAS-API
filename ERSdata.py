from .FAS_API import AlphaVantage as av


class CryptoCurrencies(av):
    """This class implements all the crypto currencies api calls
    """
    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_daily(self, symbol, market):

        _FUNCTION_KEY = 'DIGITAL_CURRENCY_DAILY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Daily)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_weekly(self, symbol, market):

        _FUNCTION_KEY = 'DIGITAL_CURRENCY_WEEKLY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Weekly)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_monthly(self, symbol, market):

        _FUNCTION_KEY = 'DIGITAL_CURRENCY_MONTHLY'
        return _FUNCTION_KEY, 'Time Series (Digital Currency Monthly)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_digital_currency_exchange_rate(self, from_currency, to_currency):

        _FUNCTION_KEY = 'CURRENCY_EXCHANGE_RATE'
        return _FUNCTION_KEY, 'Realtime Currency Exchange Rate', 'Meta Data'
    ##'Dictonary (Digital Currency Exchange Rate)'

    @av._output_format
    @av._call_api_on_func
    def get_digital_crypto_intraday(self, symbol, market, interval='60min', outputsize='compact'):

        _FUNCTION_KEY = 'CRYPTO_INTRADAY'
        return _FUNCTION_KEY, "Time Series Crypto ({})".format(interval), 'Meta Data'