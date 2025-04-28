import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
from functools import lru_cache
from nltk.tokenize import word_tokenize
import contractions

@lru_cache()
def get_nlp():
    return spacy.load('en_core_web_sm')

@lru_cache()
def get_stop_words():
    return set(stopwords.words('english'))

def clean_text(text: str):
    # Expand contractions
    text = contractions.fix(text)
    
    # Lowercase the text
    text = text.lower()

    text = text.replace("’", "'" )

    # Remove special characters and digits
    text = re.sub(r"[^a-zA-Z'\s]", '', text)
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stop words
    tokens = [word for word in tokens if word not in get_stop_words()]
    
    # Rejoin tokens to form cleaned text
    cleaned_text = ' '.join(tokens)

    return cleaned_text

#reduce words to base or dictionary form
def lemmatize_text(text):

    doc = get_nlp()

    doc = doc(text)

    lemmatized_text = ' '.join([token.lemma_ for token in doc])

    return lemmatized_text



# 예시
# sample_text = "AMD’s AI story was already <b>‘tenuous,’</b> and now the stock has new challenges."
# cleaned_text = minimal_cleaning(sample_text, to_lower=True)
# print(cleaned_text)    
