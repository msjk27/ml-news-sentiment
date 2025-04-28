import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
from functools import lru_cache
from nltk.tokenize import word_tokenize
import contractions
import unicodedata

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

def minimal_cleaning(text: str, to_lower: bool = False) -> str:
    # 1. Unicode 정규화 (예: “’”를 "'"로 바꾸기)
    text = unicodedata.normalize("NFKC", text)
    
    # 2. HTML 태그 제거 (예: <br> 같은 것)
    text = re.sub(r'<.*?>', '', text)
    
    # 3. 특수문자 중 "정상적이지 않은 것"만 제거
    # (영어 알파벳, 숫자, 일반적인 문장 부호만 살려둔다)
    text = re.sub(r'[^\w\s.,!?\'"-]', '', text)
    
    # 4. 대소문자 조정
    if to_lower:
        text = text.lower()

    return text

# 예시
sample_text = "AMD’s AI story was already <b>‘tenuous,’</b> and now the stock has new challenges."
cleaned_text = minimal_cleaning(sample_text, to_lower=True)
print(cleaned_text)    
