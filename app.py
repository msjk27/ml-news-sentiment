from src.crawling.news_api_fetcher import fetch_news_info
from src.preprocessing.clean_text import clean_text, lemmatize_text
from src.labeling.label_market_movement import label_multiple_news
from src.data.fetch_stock_data import fetch_stock_data
from src.config import API_KEY


date = '2025-04-22'
params = {
    'q': 'Apple',  # changeable
    'language': 'en',
    'sortBy': 'publishedAt',
    'from': date,
    'to': date,
    'apiKey': API_KEY,
    'pageSize': 100,
    'page': 1,
}

def main():
    df = fetch_news_info(params)
    stock_data = fetch_stock_data('AAPL', date)
    labeled_news_df = label_multiple_news(df,stock_data)
    # if titles:
    #     cleaned_titles = [clean_text(t) for t in titles]

    return labeled_news_df

a = main()
print(len(a))
# a = main()
# print(len(a))
# print(b[0:5])

