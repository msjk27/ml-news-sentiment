from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

def get_sentiment_score(text:str):
    
    sid = SentimentIntensityAnalyzer()
    
    return sid.polarity_scores(text)
