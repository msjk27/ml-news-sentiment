from src.preprocessing.sentiment_utils import get_sentiment_score
import pandas as pd

def label_market_movement(news_title: str, news_date: str, stock_data: pd.DataFrame):
    
    sentiment = get_sentiment_score(news_title)
    compound_score = sentiment['compound']

    current_close = stock_data.loc[stock_data['Date'] == news_date, 'Close'].values
    next_day_close = stock_data.loc[stock_data['Date'] > news_date, 'Close'].head(1).values

    if len(current_close) == 0 or len(next_day_close) == 0:
        return None 

    current_close = current_close[0]
    next_day_close = next_day_close[0]

    #수익률
    return_rate = (next_day_close - current_close) / current_close

    if return_rate > 0.001:
        label = 1  
    elif return_rate < -0.001:
        label = -1  
    else:
        label = 0  

    return {
        "text": news_title,
        "sentiment_score": compound_score,
        "return_rate": return_rate,
        "label": label
    }

def label_multiple_news(news_df: pd.DataFrame, stock_data: pd.DataFrame):

    labeled_data = []

    for _, row in news_df.iterrows():
        result = label_market_movement(
            news_text=row['text'],
            stock_data=stock_data,
            news_date=row['date']
        )
        if result:
            labeled_data.append(result)

    return pd.DataFrame(labeled_data)


