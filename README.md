# Yahoo-Finance-Historical-Data

The objective of this project is to facilitate the access to the historical information (stock price, dividend and split) from Yahoo Finance website and show them in a Pandas Dataframe.

1 - How To Create a object:
    test = yfhd('AAPL', '13/12/1980', '07/08/2021', '1d')
    where:

    'AAPL' is the ticker;

    '13/12/1980' is the beggin date;

    '07/08/2021' is the last date;

    '1d' is the frequenci of information, it can be '1wk' (week), '1mo' (month)

2 - Getting information (return a Pandas Dataframe):

    test.show_history_data()

    test.show_div_data()

    test.show_split_data()


3 - Getting the status of conection:
    test.show_history_status()

    test.show_div_status()

    test.show_split_status()

    **All the status: https://httpstatuses.com/

