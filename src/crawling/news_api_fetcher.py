#!/usr/bin/env python3
from src.config.config import NEWS_API_URL, API_KEY
import requests

# Crawling finance news from NewsApi
def fetch_news_info(params: dict[str,str|int]) :
    
    response = requests.get(NEWS_API_URL, params = params)

    if response.status_code == 200:
        data = response.json()
        titles = [article['title'] for article in data.get('articles', [])]
        return titles

    else:
        print(f"Error: {response.status_code}")
        return []
