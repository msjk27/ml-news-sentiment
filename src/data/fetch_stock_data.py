import yfinance as yf
import pandas as pd


def fetch_stock_data(stock_name:str, date:str):
    
    start_date = pd.to_datetime(date)

    end_date = end_date = start_date + pd.Timedelta(days=10)

    #yf.download는 column 을 index 로 설정함. '.rest_index()' 로 column 으로 바꿔줌
    stock_data = (yf.download(stock_name, start= start_date, end= end_date)).reset_index()

    return (stock_data)

