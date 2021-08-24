import requests
from datetime import datetime
import pandas as pd
import numpy as np


class yfhd:
    def __init__(self, ticker: str, period1: str, period2: str, interval: str):
        self.ticker: str = ticker
        self.period1: str = self.convert_date(period1)
        self.period2: str = self.convert_date(period2)
        self.interval: str = self.validate_interval(interval)
        self.headers: dict = {'User-Agent': 'None'}
        self.history_data: requests.models.Responses = self.get_history_data()
        self.dividend_data = ''
        self.split_data = ''

    def str_to_dataframe(self, string_var: str) -> pd.DataFrame:
        string_var = string_var.split('\n')
        for aux in range(len(string_var)):
            string_var[aux] = string_var[aux].split(',')
        df_string_var = pd.DataFrame(np.array(string_var[1:]), columns=string_var[0])
        df_string_var['Date'] = pd.to_datetime(df_string_var['Date'],
                                format='%Y-%m-%d', errors='coerce')
        return df_string_var

    def show_history_data(self) -> str:
        return self.str_to_dataframe(self.history_data.text)

    def show_history_status(self) -> str:
        return self.history_data.status_code

    def get_history_data(self) -> requests.models.Response:
        self.events = 'history'
        self.url = 'https://query1.finance.yahoo.com/v7/finance/download/' +\
                    self.ticker + '?period1=' + self.period1 + '&period2=' +\
                    self.period2 + '&interval=' + self.interval + '&events='\
                    + self.events + '&includeAdjustedClose=true'
        return requests.get(self.url, headers=self.headers)

    def convert_date(self, date_value: str) -> str:
        try:
            date_value_aux =  datetime.strptime(date_value, '%d/%m/%Y')
            date_reference = datetime.strptime('02/01/1962', '%d/%m/%Y')
            if date_reference > date_value_aux:
                return ValueError('The minimum date allowed is 02/01/1962')
            else:
                num_days = date_value_aux - date_reference
                return str(-252374400 + (num_days.days * 24 * 60 * 60))
        except:
            return ValueError(f'Problem with {date_value}')
        
    def validate_interval(self, interval: str) -> str:
        if interval in ['1d', '1w', '1wk', '1mo']:
            return interval
        else:
            return ValueError(f'{interval} Interval must be equal to 1d, 1wk or 1mo')


if __name__ == '__main__':
    teste = yfhd('AAPL', '05/07/2021', '07/08/2021', '1d')
    print(teste.show_history_data())
    

