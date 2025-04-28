import yfinance as yf
import pandas as pd


def fetch_stock_data(stock_name:str, date:str):

    return (yf.download(stock_name, start= date, end= date))

