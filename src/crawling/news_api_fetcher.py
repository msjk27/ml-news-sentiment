#!/usr/bin/env python3
from src.config.config import NEWS_API_URL
import pandas as pd
import requests

# Crawling finance news from NewsApi
def fetch_news_info(params: dict[str,str|int]) -> pd.DataFrame :

    response = requests.get(NEWS_API_URL, params = params)

    records = []
    if response.status_code == 200:

        data = response.json()
        articles = data.get('articles', [])

        records = []

        for article in articles:
            record = {
                'title': article.get('title'),
                'date': pd.to_datetime(article.get('publishedAt')).date()
            }
            print(record['date'])
            records.append(record)

        return pd.DataFrame(records)

    else:
        return pd.DataFrame(columns=['title', 'date'])