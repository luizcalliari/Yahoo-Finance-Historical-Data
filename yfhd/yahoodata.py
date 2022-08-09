import numpy as np
import pandas as pd
import requests

from datetime import datetime
from typing import Optional, Union


class YahooData:
    def __init__(self, ticker: str, period1: str, period2: str, interval: str):
        self.url: Optional[str] = None
        self.ticker: str = ticker
        self.period1: str = self._convert_date(date_value=period1)
        self.period2: str = self._convert_date(date_value=period2)
        self.interval: str = self._validate_interval(interval=interval)
        self.headers: dict = {'User-Agent': 'None'}
        self.history_data: requests = self._get_data(events='history')
        self.dividend_data: requests = self._get_data(events='div')
        self.split_data: requests = self._get_data(events='split')

    def _str_to_dataframe(self, string_var: str) -> Union[pd.DataFrame, str]:
        string_var = string_var.split('\n')
        if len(string_var) > 1:
            string_aux = []
            for aux in string_var:
                string_aux.append(aux.split(','))
            df_string_var = pd.DataFrame(np.array(string_aux[1:]), columns=string_aux[0])
            df_string_var['Date'] = pd.to_datetime(df_string_var['Date'], format='%Y-%m-%d', errors='coerce')
        else:
            df_string_var = 'empty'

        return df_string_var

    def show_split_data(self) -> pd.DataFrame:
        return self._str_to_dataframe(string_var=self.split_data.text)

    def show_split_status(self) -> int:
        return self.split_data.status_code

    def show_div_data(self) -> pd.DataFrame:
        return self._str_to_dataframe(string_var=self.dividend_data.text)

    def show_div_status(self) -> int:
        return self.dividend_data.status_code

    def show_history_data(self) -> pd.DataFrame:
        return self._str_to_dataframe(string_var=self.history_data.text)

    def show_history_status(self) -> int:
        return self.history_data.status_code

    def _get_data(self, events: str) -> requests:
        self.url = (
            'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}'
            '&interval={interval}&events={events}&includeAdjustedClose=true'
        ).format(ticker=self.ticker, period1=self.period1, period2=self.period2, interval=self.interval, events=events)

        return requests.get(self.url, headers=self.headers)

    def _convert_date(self, date_value: str) -> str:
        try:
            date_value_aux = datetime.strptime(date_value, '%d/%m/%Y')
        except Exception as e:
            raise ValueError(f'Problem with {date_value}')
        else:
            date_reference = datetime.strptime('02/01/1962', '%d/%m/%Y')
            if date_reference > date_value_aux:
                raise ValueError('The minimum date allowed is 02/01/1962')
            else:
                num_days = date_value_aux - date_reference

                return str(-252374400 + (num_days.days * 24 * 60 * 60))

    def _validate_interval(self, interval: str) -> str:
        if interval in ['1d', '1wk', '1mo']:
            return interval
        else:
            raise ValueError(f'{interval} Interval must be 1d, 1wk or 1mo')


if __name__ == '__main__':
    test = YahooData('AAPL', '13/12/1980', '07/08/2021', '1d')
    print(test.show_history_status())
    print(test.show_history_data())
    print(test.show_div_status())
    print(test.show_div_data())
    print(test.show_split_status())
    print(test.show_split_data())
