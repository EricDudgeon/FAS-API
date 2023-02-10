from .FAS_API import AlphaVantage as av


class TimeSeries(av):

    """This class implements all the api calls to times series
    """
    @av._output_format
    @av._call_api_on_func
    def get_intraday(self, symbol, interval='15min', outputsize='compact'):

        _FUNCTION_KEY = "TIME_SERIES_INTRADAY"
        return _FUNCTION_KEY, "Time Series ({})".format(interval), 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_daily(self, symbol, outputsize='compact'):

        _FUNCTION_KEY = "TIME_SERIES_DAILY"
        return _FUNCTION_KEY, 'Time Series (Daily)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_daily_adjusted(self, symbol, outputsize='compact'):

        _FUNCTION_KEY = "TIME_SERIES_DAILY_ADJUSTED"
        return _FUNCTION_KEY, 'Time Series (Daily)', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_weekly(self, symbol):

        _FUNCTION_KEY = "TIME_SERIES_WEEKLY"
        return _FUNCTION_KEY, 'Weekly Time Series', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_weekly_adjusted(self, symbol):

        _FUNCTION_KEY = "TIME_SERIES_WEEKLY_ADJUSTED"
        return _FUNCTION_KEY, 'Weekly Adjusted Time Series', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_monthly(self, symbol):

        _FUNCTION_KEY = "TIME_SERIES_MONTHLY"
        return _FUNCTION_KEY, 'Monthly Time Series', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_monthly_adjusted(self, symbol):

        _FUNCTION_KEY = "TIME_SERIES_MONTHLY_ADJUSTED"
        return _FUNCTION_KEY, 'Monthly Adjusted Time Series', 'Meta Data'

    @av._output_format
    @av._call_api_on_func
    def get_quote_endpoint(self, symbol):

        _FUNCTION_KEY = "GLOBAL_QUOTE"
        return _FUNCTION_KEY, 'Global Quote', None

    @av._output_format
    @av._call_api_on_func
    def get_symbol_search(self, keywords):

        _FUNCTION_KEY = "SYMBOL_SEARCH"
        return _FUNCTION_KEY, 'bestMatches', None
