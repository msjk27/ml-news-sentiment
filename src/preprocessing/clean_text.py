import re
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
from functools import lru_cache
from nltk.tokenize import word_tokenize

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

@lru_cache()
def get_nlp():
    return spacy.load('en_core_web_sm')

@lru_cache()
def get_stop_words():
    return set(stopwords.words('english'))

def clean_text(text: str):
  text = text.lower()

  #Remove special characters and digits
  text = re.sub(r'[^a-zA-Z\s]', '', text)

  #list of word in text
  tokens = word_tokenize(text)

  #remove stop words, like the, a, etc
  tokens = [word for word in tokens if word not in get_stop_words()]

  cleaned_text = ' '.join(tokens)

  return cleaned_text

#reduce words to base or dictionary form
def lemmatize_text(text):

    doc = get_nlp()

    doc = doc(text)

    lemmatized_text = ' '.join([token.lemma_ for token in doc])

    return lemmatized_text

# text = "running is very happy I am good. I want to run all day"
# print("okay")
# text = clean_text(text)
# text = lemmatize_text(text)
# print(text)