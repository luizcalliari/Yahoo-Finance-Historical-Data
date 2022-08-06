import requests
from datetime import datetime
import pandas as pd
import numpy as np


class YahooData:
    def __init__(self, ticker: str, period1: str, period2: str, interval: str):
        self.ticker: str = ticker
        self.period1: str = self.convert_date(period1)
        self.period2: str = self.convert_date(period2)
        self.interval: str = self.validate_interval(interval)
        self.headers: dict = {'User-Agent': 'None'}
        self.history_data: requests.models.Responses = self.get_data('history')
        self.dividend_data: requests.models.Responses = self.get_data('div')
        self.split_data: requests.models.Responses = self.get_data('split')

    def str_to_dataframe(self, string_var: str) -> pd.DataFrame:
        string_var = string_var.split('\n')
        if len(string_var) > 1:
            for aux in range(len(string_var)):
                string_var[aux] = string_var[aux].split(',')
            df_string_var = pd.DataFrame(np.array(string_var[1:]), columns=string_var[0])
            df_string_var['Date'] = pd.to_datetime(df_string_var['Date'],
                                    format='%Y-%m-%d', errors='coerce')
        else:
            df_string_var = 'empty'
        return df_string_var

    def show_split_data(self) -> str:
        return self.str_to_dataframe(self.split_data.text)

    def show_split_status(self) -> str:
        return self.split_data.status_code

    def show_div_data(self) -> str:
        return self.str_to_dataframe(self.dividend_data.text)

    def show_div_status(self) -> str:
        return self.dividend_data.status_code

    def show_history_data(self) -> str:
        return self.str_to_dataframe(self.history_data.text)

    def show_history_status(self) -> str:
        return self.history_data.status_code

    def get_data(self, events: str) -> requests.models.Response:
        self.url = 'https://query1.finance.yahoo.com/v7/finance/download/' +\
                    self.ticker + '?period1=' + self.period1 + '&period2=' +\
                    self.period2 + '&interval=' + self.interval + '&events='\
                    + events + '&includeAdjustedClose=true'
        return requests.get(self.url, headers=self.headers)

    def convert_date(self, date_value: str) -> str:
        try:
            date_value_aux =  datetime.strptime(date_value, '%d/%m/%Y')
            date_reference = datetime.strptime('02/01/1962', '%d/%m/%Y')
            if date_reference > date_value_aux:
                raise ValueError('The minimum date allowed is 02/01/1962')
            else:
                num_days = date_value_aux - date_reference
                return str(-252374400 + (num_days.days * 24 * 60 * 60))
        except:
            raise ValueError(f'Problem with {date_value}')
        
    def validate_interval(self, interval: str) -> str:
        if interval in ['1d', '1wk', '1mo']:
            return interval
        else:
            raise ValueError(f'{interval} Interval must be equal to 1d, 1wk or 1mo')


if __name__ == '__main__':
    test = YahooData('AAPL', '13/12/1980', '07/08/2021', '1d')
    print(test.show_history_status())
    print(test.show_history_data())
    print(test.show_div_status())
    print(test.show_div_data())
    print(test.show_split_status())
    print(test.show_split_data())

