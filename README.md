# Yahoo-Finance-Historical-Data

## Instaling
    python setup.py install

## Requirements
* Python >= 3.8

## Description
The objective of this project is to facilitate the access to the historical information (stock price, dividend and 
split) from Yahoo Finance website and show them in a Pandas Dataframe.

1 - How To Create a object:
    <code>test = yfhd('AAPL', '13/12/1980', '07/08/2021', '1d')</code>

    'AAPL' is the ticker;

    '13/12/1980' is the beggin date;

    '07/08/2021' is the last date;

    '1d' is the frequenci of information, it can be '1wk' (week), '1mo' (month)

2 - Getting information (return a Pandas Dataframe):

    test.show_history_data()

    test.show_div_data()

    test.show_split_data()

3 - Getting the status of connection (<a href="https://httpstatuses.com/">All the response status</a>)
    
    test.show_history_status()

    test.show_div_status()

    test.show_split_status()
