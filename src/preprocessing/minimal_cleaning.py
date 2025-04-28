import unicodedata
import re

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