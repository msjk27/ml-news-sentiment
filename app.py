from src.crawling.news_api_fetcher import fetch_news_info
from src.preprocessing.clean_text import clean_text, lemmatize_text
from src.config import API_KEY

params = {
    'q': 'iphone',  # changeable
    'language': 'en',
    'sortBy': 'publishedAt',
    'from': '2025-04-01',
    'to': '2025-04-22',
    'apiKey': API_KEY,
    'pageSize': 100
}

def main():
    
    titles = fetch_news_info(params)
    
    if titles:
        cleaned_titles = [clean_text(t) for t in titles]

    return titles,cleaned_titles

# a,b = main()
# print(a[0:5])
# print(b[0:5])

