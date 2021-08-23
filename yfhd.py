import requests
from datetime import datetime
#import pandas as pd


class Yahoo_Data:
    def __init__(self, ticker: str, period1: str, period2: str, interval: str):
        self.ticker: str = ticker
        self.period1: str = self.convert_date(period1)
        self.period2: str = self.convert_date(period2)
        self.interval: str = self.validate_interval(interval)
        self.headers = {'User-Agent': 'None'}
        self.history_data = ''
        self.dividend_data = ''
        self.split_data = ''

    def get_valor(self):
        print('history data')
        print(type(self.history_data))
        print(self.history_data)
        print(f'period1: {self.period1}')
        print(f'period2: {self.period2}')

    def get_history_data(self):
        self.events = 'history'
        self.url = 'https://query1.finance.yahoo.com/v7/finance/download/' +\
                    self.ticker + '?period1=' + self.period1 + '&period2=' +\
                    self.period2 + '&interval=' + self.interval + '&events='\
                    + self.events + '&includeAdjustedClose=true'
        self.history_data = requests.get(self.url, headers=self.headers)

    def get_texto(self):
        print(self.history_data.status_code)
        print(self.history_data.text)
        print(type(self.history_data.text))

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
            return ValueError(f'{interval} Interval must be equal to 1w, 1wk or 1mo')


if __name__ == '__main__':
    teste = Yahoo_Data('AAPL', '05/08/2021', '07/08/2021', '1d')
    teste.get_history_data()
    teste.get_texto()



