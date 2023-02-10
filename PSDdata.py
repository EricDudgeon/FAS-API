from .FAS_API import AlphaVantage as av


class ForeignExchange(av):


    def __init__(self, *args, **kwargs):
        """
        Inherit base class with its default arguments
        """
        super(ForeignExchange, self).__init__(*args, **kwargs)
        self._append_type = False
        if self.output_format.lower() == 'csv':
            raise ValueError("Output format {} is not compatible with the ForeignExchange class".format(
                self.output_format.lower()))

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_rate(self, from_currency, to_currency):

        _FUNCTION_KEY = 'CURRENCY_EXCHANGE_RATE'
        return _FUNCTION_KEY, 'Realtime Currency Exchange Rate', None

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_intraday(self, from_symbol, to_symbol, interval='15min', outputsize='compact'):

        _FUNCTION_KEY = 'FX_INTRADAY'
        return _FUNCTION_KEY, "Time Series FX ({})".format(interval), 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_daily(self, from_symbol, to_symbol, outputsize='compact'):

        _FUNCTION_KEY = 'FX_DAILY'
        return _FUNCTION_KEY, "Time Series FX (Daily)", 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_weekly(self, from_symbol, to_symbol, outputsize='compact'):

        _FUNCTION_KEY = 'FX_WEEKLY'
        return _FUNCTION_KEY, "Time Series FX (Weekly)", 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_currency_exchange_monthly(self, from_symbol, to_symbol, outputsize='compact'):

        _FUNCTION_KEY = 'FX_MONTHLY'
        return _FUNCTION_KEY, "Time Series FX (Monthly)", 'Meta Data'
