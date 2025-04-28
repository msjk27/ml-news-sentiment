from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

def get_sentiment_score(text:str):
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores("amd 's ai story already tenuous ' stock new challenges")
    print(sentiment)