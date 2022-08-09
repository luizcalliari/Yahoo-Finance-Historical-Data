import pytest
import numpy as np
import pandas as pd

from yfhd.yahoodata import YahooData


@pytest.fixture
def yfhd_apple_stock():
    return YahooData('AAPL', '13/12/1980', '16/12/1980', '1d')


def test_history_connection(yfhd_apple_stock):
    assert yfhd_apple_stock.show_history_status() == 200


def test_div_connection(yfhd_apple_stock):
    assert yfhd_apple_stock.show_div_status() == 200


def test_split_connection(yfhd_apple_stock):
    assert yfhd_apple_stock.show_split_status() == 200


def test_period1_conversion(yfhd_apple_stock):
    assert yfhd_apple_stock.period1 == '345513600'


def test_period1_conversion(yfhd_apple_stock):
    assert yfhd_apple_stock.period2 == '345772800'


def test_history_type_output(yfhd_apple_stock):
    assert isinstance(yfhd_apple_stock.show_history_data(), pd.DataFrame)


def test_div_type_output(yfhd_apple_stock):
    assert isinstance(yfhd_apple_stock.show_div_data(), str)


def test_split_type_output(yfhd_apple_stock):
    assert isinstance(yfhd_apple_stock.show_split_data(), str)


def test_history_data(yfhd_apple_stock):
    values = [
        ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'],
        ['1980-12-15', '0.122210', '0.122210', '0.121652', '0.121652', '0.094820', '175884800']
    ]
    expected_result = pd.DataFrame(np.array(values[1:]), columns=values[0])
    expected_result['Date'] = pd.to_datetime(expected_result['Date'], format='%Y-%m-%d', errors='coerce')
    result = yfhd_apple_stock.show_history_data()

    pd.testing.assert_frame_equal(result, expected_result)
