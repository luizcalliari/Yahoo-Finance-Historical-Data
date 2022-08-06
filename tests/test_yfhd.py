import pytest
from yfhd.yahoodata import YahooData
import pandas


@pytest.fixture
def yfhd_apple_stock():
    return YahooData('AAPL', '13/12/1980', '07/08/2021', '1d')


def test_history_connection(yfhd_apple_stock):
    assert yfhd_apple_stock.show_history_status() == 200


def test_div_connection(yfhd_apple_stock):
    assert yfhd_apple_stock.show_div_status() == 200


def test_split_connection(yfhd_apple_stock):
    assert yfhd_apple_stock.show_split_status() == 200


def test_period1_conversion(yfhd_apple_stock):
    assert yfhd_apple_stock.period1 == '345513600'


def test_period1_conversion(yfhd_apple_stock):
    assert yfhd_apple_stock.period2 == '1628294400'


def test_history_type_output(yfhd_apple_stock):
    assert type(yfhd_apple_stock.show_history_data()) == pandas.core.frame.DataFrame


def test_div_type_output(yfhd_apple_stock):
    assert type(yfhd_apple_stock.show_div_data()) == pandas.core.frame.DataFrame


def test_split_type_output(yfhd_apple_stock):
    assert type(yfhd_apple_stock.show_split_data()) == pandas.core.frame.DataFrame
